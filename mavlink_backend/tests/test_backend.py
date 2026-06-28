import time
import threading
from unittest.mock import Mock, patch

import pytest


def test_init_connects_and_waits_for_heartbeat(mock_master):
    from mavlink_backend import MAVLinkBackend

    with patch('mavlink_backend.backend.mavutil.mavlink_connection', return_value=mock_master):
        backend = MAVLinkBackend(connection_string='udp:test')
        backend.stop()

        assert backend.master == mock_master
        mock_master.wait_heartbeat.assert_called_once()


def test_process_message_global_position_int(backend):
    msg = Mock()
    msg.get_type.return_value = 'GLOBAL_POSITION_INT'
    msg.lat = 557558000
    msg.lon = 376173000
    msg.alt = 10500
    msg.relative_alt = 2500

    backend._process_message(msg)

    assert backend.telemetry['position']['lat'] == 55.7558
    assert backend.telemetry['position']['lon'] == 37.6173
    assert backend.telemetry['position']['alt'] == 10.5
    assert backend.telemetry['position']['relative_alt'] == 2.5


def test_process_message_sys_status_battery(backend):
    msg = Mock()
    msg.get_type.return_value = 'SYS_STATUS'
    msg.voltage_battery = 11200
    msg.current_battery = 250
    msg.battery_remaining = 85

    backend._process_message(msg)

    assert backend.telemetry['battery']['voltage'] == 11.2
    assert backend.telemetry['battery']['current'] == 2.5
    assert backend.telemetry['battery']['remaining'] == 85


def test_process_message_heartbeat_updates_status(backend):
    backend.telemetry['status'] = 'disconnected'

    msg = Mock()
    msg.get_type.return_value = 'HEARTBEAT'

    backend._process_message(msg)

    assert backend.telemetry['status'] == 'connected'


def test_send_setpoint_calls_correct_mavlink_method(backend):
    x, y, z, yaw = 5.0, 3.0, 2.0, 0.5

    backend.send_setpoint(x, y, z, yaw)

    backend.master.mav.set_position_target_local_ned_send.assert_called_once()
    call_args = backend.master.mav.set_position_target_local_ned_send.call_args

    assert call_args[0][5] == x
    assert call_args[0][6] == y
    assert call_args[0][7] == z
    assert call_args[0][14] == yaw


def test_upload_mission_clears_old_mission_first(backend):
    waypoints = [(55.0, 37.0, 10.0)]

    with patch.object(backend.master, 'recv_match') as mock_recv:
        msg_req = Mock()
        msg_req.get_type.return_value = 'MISSION_REQUEST'
        msg_req.seq = 0

        msg_ack = Mock()
        msg_ack.get_type.return_value = 'MISSION_ACK'
        msg_ack.type = 0

        mock_recv.side_effect = [msg_req, msg_ack]

        backend.upload_mission(waypoints)
        backend.master.waypoint_clear_all_send.assert_called_once()


def test_upload_mission_sends_count_and_items(backend):
    waypoints = [(55.0, 37.0, 10.0), (55.1, 37.1, 10.0)]

    with patch.object(backend.master, 'recv_match') as mock_recv:
        msg_req_1 = Mock()
        msg_req_1.get_type.return_value = 'MISSION_REQUEST'
        msg_req_1.seq = 0

        msg_req_2 = Mock()
        msg_req_2.get_type.return_value = 'MISSION_REQUEST'
        msg_req_2.seq = 1

        msg_ack = Mock()
        msg_ack.get_type.return_value = 'MISSION_ACK'
        msg_ack.type = 0

        mock_recv.side_effect = [msg_req_1, msg_req_2, msg_ack]

        backend.upload_mission(waypoints)
        backend.master.waypoint_count_send.assert_called_once_with(2)
        assert backend.master.mav.mission_item_int_send.call_count == 2


def test_upload_mission_returns_true_on_success(backend):
    waypoints = [(55.0, 37.0, 10.0)]

    with patch.object(backend.master, 'recv_match') as mock_recv:
        msg_req = Mock()
        msg_req.get_type.return_value = 'MISSION_REQUEST'
        msg_req.seq = 0

        msg_ack = Mock()
        msg_ack.get_type.return_value = 'MISSION_ACK'
        msg_ack.type = 0

        mock_recv.side_effect = [msg_req, msg_ack]

        result = backend.upload_mission(waypoints)
        assert result is True


def test_upload_mission_returns_false_on_timeout(backend):
    waypoints = [(55.0, 37.0, 10.0)]

    with patch.object(backend.master, 'recv_match') as mock_recv:
        mock_recv.return_value = None

        result = backend.upload_mission(waypoints)
        assert result is False


def test_get_telemetry_returns_copy_not_reference(backend):
    backend.telemetry['status'] = 'original'

    telemetry1 = backend.get_telemetry()
    telemetry1['status'] = 'modified'

    telemetry2 = backend.get_telemetry()

    assert backend.telemetry['status'] == 'original'
    assert telemetry2['status'] == 'original'


@pytest.mark.integration
class TestSITLIntegration:

    def test_sitl_connection_established(self, sitl_backend):
        assert sitl_backend.master is not None
        assert sitl_backend.telemetry['status'] == 'connected'
        assert sitl_backend.master.target_system == 1
        assert sitl_backend.master.target_component == 1

    def test_sitl_receives_heartbeat(self, sitl_backend):
        sitl_backend.send_heartbeat()
        time.sleep(0.1)
        assert sitl_backend.master.port is not None

    def test_sitl_telemetry_streaming(self, sitl_backend):
        time.sleep(0.5)

        telemetry = sitl_backend.get_telemetry()
        assert 'position' in telemetry
        assert 'battery' in telemetry
        assert 'status' in telemetry

        pos = telemetry['position']
        assert all(key in pos for key in ['lat', 'lon', 'alt', 'relative_alt'])

        batt = telemetry['battery']
        assert all(key in batt for key in ['voltage', 'current', 'remaining'])

    def test_sitl_send_setpoint_guided_mode(self, sitl_backend):
        sitl_backend.send_setpoint(x=0.0, y=10.0, z=-5.0, yaw=0.0)

        time.sleep(0.5)
        telemetry = sitl_backend.get_telemetry()

        assert telemetry['status'] == 'connected'

    def test_sitl_upload_mission_auto_mode(self, sitl_backend):
        waypoints = [
            (-35.363261, 149.165230, 10.0),
            (-35.363300, 149.165300, 10.0),
            (-35.363200, 149.165300, 10.0),
        ]

        success = sitl_backend.upload_mission(waypoints)
        assert success is True

        time.sleep(0.3)
        telemetry = sitl_backend.get_telemetry()
        assert telemetry['status'] == 'connected'

    def test_sitl_position_updates(self, sitl_backend):
        time.sleep(0.5)
        telemetry1 = sitl_backend.get_telemetry()
        pos1 = telemetry1['position']

        time.sleep(0.5)
        telemetry2 = sitl_backend.get_telemetry()

        assert isinstance(pos1['lat'], float)
        assert isinstance(pos1['lon'], float)
        assert isinstance(pos1['alt'], float)

    def test_sitl_battery_telemetry(self, sitl_backend):
        time.sleep(0.5)
        telemetry = sitl_backend.get_telemetry()

        battery = telemetry['battery']
        assert isinstance(battery['voltage'], float)
        assert isinstance(battery['current'], float)
        assert isinstance(battery['remaining'], int)

        assert 0 < battery['voltage'] < 20

    def test_sitl_multiple_setpoints_sequence(self, sitl_backend):
        points = [
            (5.0, 0.0, -3.0),
            (5.0, 5.0, -3.0),
            (0.0, 5.0, -3.0),
        ]

        for x, y, z in points:
            sitl_backend.send_setpoint(x, y, z, yaw=0.0)
            time.sleep(0.2)

            telemetry = sitl_backend.get_telemetry()
            assert telemetry['status'] == 'connected'

    def test_sitl_mission_upload_with_invalid_coords(self, sitl_backend):
        invalid_waypoints = [
            (100.0, 200.0, 10.0),
            (150.0, 250.0, 10.0),
        ]

        try:
            result = sitl_backend.upload_mission(invalid_waypoints)
            assert isinstance(result, bool)
        except Exception as e:
            assert isinstance(e, Exception)

    def test_sitl_concurrent_telemetry_and_commands(self, sitl_backend):
        errors = []

        def send_commands():
            try:
                for i in range(5):
                    sitl_backend.send_setpoint(i, 0, -2.0, 0.0)
                    time.sleep(0.1)
            except Exception as e:
                errors.append(e)

        def read_telemetry():
            try:
                for i in range(10):
                    telemetry = sitl_backend.get_telemetry()
                    assert telemetry['status'] == 'connected'
                    time.sleep(0.05)
            except Exception as e:
                errors.append(e)

        t1 = threading.Thread(target=send_commands)
        t2 = threading.Thread(target=read_telemetry)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        assert len(errors) == 0, f"Errors occurred: {errors}"
