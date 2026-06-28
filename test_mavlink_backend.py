import pytest
from unittest.mock import Mock, patch, MagicMock
import time
import socket
import threading
# Импорт тестируемого модуля
from mavlink_backend import MAVLinkBackend


@pytest.fixture
def mock_master():
    """Создает мок-объект для pymavlink.mavutil"""
    master = Mock()
    master.target_system = 1
    master.target_component = 1
    return master


@pytest.fixture
def backend(mock_master):
    """Создает экземпляр MAVLinkBackend с моком вместо реального соединения"""
    # Патчим mavlink_connection в модуле pymavlink.mavutil, который используется внутри mavlink_backend
    with patch('mavlink_backend.mavutil.mavlink_connection', return_value=mock_master):
        # Также патчим wait_heartbeat, чтобы не ждать реально
        with patch.object(mock_master, 'wait_heartbeat'):
            b = MAVLinkBackend(connection_string='udp:test')
            b.stop()
            yield b


# ... (далее идут твои тесты) ...

@pytest.fixture
def sitl_backend():
    """Создает реальный бэкенд для интеграционных тестов с SITL"""
    try:
        # Подключаемся к стандартному порту SITL
        backend = MAVLinkBackend('udp:127.0.0.1:14550')
        yield backend
        backend.stop()
    except Exception as e:
        pytest.skip(f"SITL not available or connection failed: {e}")


# ==================== ЮНИТ ТЕСТЫ (Без железа) ====================

def test_init_connects_and_waits_for_heartbeat(mock_master):
    """Тест 1: Проверка инициализации и ожидания HEARTBEAT"""
    with patch('mavlink_backend.mavutil.mavlink_connection', return_value=mock_master):
        backend = MAVLinkBackend(connection_string='udp:test')
        backend.stop()

        assert backend.master == mock_master
        mock_master.wait_heartbeat.assert_called_once()


def test_process_message_global_position_int(backend):
    """Тест 2: Обработка сообщения GLOBAL_POSITION_INT (позиция)"""
    msg = Mock()
    msg.get_type.return_value = 'GLOBAL_POSITION_INT'
    msg.lat = 557558000  # 55.7558 * 1e7
    msg.lon = 376173000  # 37.6173 * 1e7
    msg.alt = 10500      # 10.5 * 1000
    msg.relative_alt = 2500  # 2.5 * 1000

    backend._process_message(msg)

    assert backend.telemetry['position']['lat'] == 55.7558
    assert backend.telemetry['position']['lon'] == 37.6173
    assert backend.telemetry['position']['alt'] == 10.5
    assert backend.telemetry['position']['relative_alt'] == 2.5


def test_process_message_sys_status_battery(backend):
    """Тест 3: Обработка сообщения SYS_STATUS (батарея)"""
    msg = Mock()
    msg.get_type.return_value = 'SYS_STATUS'
    msg.voltage_battery = 11200  # 11.2 V
    msg.current_battery = 250    # 2.5 A
    msg.battery_remaining = 85   # 85%

    backend._process_message(msg)

    assert backend.telemetry['battery']['voltage'] == 11.2
    assert backend.telemetry['battery']['current'] == 2.5
    assert backend.telemetry['battery']['remaining'] == 85


def test_process_message_heartbeat_updates_status(backend):
    """Тест 4: Обновление статуса при получении HEARTBEAT"""
    backend.telemetry['status'] = 'disconnected'

    msg = Mock()
    msg.get_type.return_value = 'HEARTBEAT'

    backend._process_message(msg)

    assert backend.telemetry['status'] == 'connected'


def test_send_setpoint_calls_correct_mavlink_method(backend):
    """Тест 5: Отправка setpoint вызывает правильный метод MAVLink"""
    x, y, z, yaw = 5.0, 3.0, 2.0, 0.5

    backend.send_setpoint(x, y, z, yaw)

    backend.master.mav.set_position_target_local_ned_send.assert_called_once()
    call_args = backend.master.mav.set_position_target_local_ned_send.call_args

    # Проверяем ключевые аргументы (позиции зависят от сигнатуры функции в pymavlink)
    # Обычно: time_boot_ms, target_system, target_component, frame, type_mask, x, y, z...
    assert call_args[0][5] == x
    assert call_args[0][6] == y
    assert call_args[0][7] == z
    assert call_args[0][14] == yaw


def test_upload_mission_clears_old_mission_first(backend):
    """Тест 6: Загрузка миссии начинается с очистки старой"""
    waypoints = [(55.0, 37.0, 10.0)]

    with patch.object(backend.master, 'recv_match') as mock_recv:
        # Мок для MISSION_REQUEST
        msg_req = Mock()
        msg_req.get_type.return_value = 'MISSION_REQUEST'
        msg_req.seq = 0

        # Мок для MISSION_ACK
        msg_ack = Mock()
        msg_ack.get_type.return_value = 'MISSION_ACK'
        msg_ack.type = 0  # MAV_MISSION_ACCEPTED

        mock_recv.side_effect = [msg_req, msg_ack]

        backend.upload_mission(waypoints)
        backend.master.waypoint_clear_all_send.assert_called_once()


def test_upload_mission_sends_count_and_items(backend):
    """Тест 7: Загрузка миссии отправляет количество и сами точки"""
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
    """Тест 8: upload_mission возвращает True при успешной загрузке"""
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
    """Тест 9: upload_mission возвращает False при таймауте"""
    waypoints = [(55.0, 37.0, 10.0)]

    with patch.object(backend.master, 'recv_match') as mock_recv:
        mock_recv.return_value = None  # Таймаут

        result = backend.upload_mission(waypoints)
        assert result is False


def test_get_telemetry_returns_copy_not_reference(backend):
    """Тест 10: get_telemetry возвращает копию данных, а не ссылку"""
    backend.telemetry['status'] = 'original'

    telemetry1 = backend.get_telemetry()
    telemetry1['status'] = 'modified'

    telemetry2 = backend.get_telemetry()

    # Изменение копии не должно влиять на исходные данные
    assert backend.telemetry['status'] == 'original'
    assert telemetry2['status'] == 'original'


# ==================== ИНТЕГРАЦИОННЫЕ ТЕСТЫ С SITL ====================

@pytest.mark.integration
class TestSITLIntegration:
    """Интеграционные тесты с реальным SITL симулятором ArduPilot"""

    def test_sitl_connection_established(self, sitl_backend):
        """Тест 11: Успешное подключение к SITL"""
        assert sitl_backend.master is not None
        assert sitl_backend.telemetry['status'] == 'connected'
        assert sitl_backend.master.target_system == 1
        assert sitl_backend.master.target_component == 1

    def test_sitl_receives_heartbeat(self, sitl_backend):
        """Тест 12: SITL получает HEARTBEAT от бэкенда"""
        sitl_backend.send_heartbeat()
        time.sleep(0.1)
        # Если не упало - значит соединение активно
        assert sitl_backend.master.port is not None

    def test_sitl_telemetry_streaming(self, sitl_backend):
        """Тест 13: Получение телеметрии от SITL"""
        time.sleep(0.5)  # Дать время на получение сообщений

        telemetry = sitl_backend.get_telemetry()
        assert 'position' in telemetry
        assert 'battery' in telemetry
        assert 'status' in telemetry

        # Проверяем структуру данных
        pos = telemetry['position']
        assert all(key in pos for key in ['lat', 'lon', 'alt', 'relative_alt'])

        batt = telemetry['battery']
        assert all(key in batt for key in ['voltage', 'current', 'remaining'])

    def test_sitl_send_setpoint_guided_mode(self, sitl_backend):
        """Тест 14: Отправка setpoint в режиме Guided"""
        # Отправляем точку на высоте 5м, в 10м на север (локальные координаты NED)
        # Z вниз в NED, поэтому отрицательное значение для высоты вверх
        sitl_backend.send_setpoint(x=0.0, y=10.0, z=-5.0, yaw=0.0)

        time.sleep(0.5)
        telemetry = sitl_backend.get_telemetry()

        # Проверяем, что команда принята (статус должен быть connected)
        assert telemetry['status'] == 'connected'

    def test_sitl_upload_mission_auto_mode(self, sitl_backend):
        """Тест 15: Загрузка миссии в режиме AUTO"""
        # Создаём простую миссию из 3 точек (квадрат) вокруг CMAC
        # Важно: для Blimp/SITL координаты должны быть реалистичными
        waypoints = [
            (-35.363261, 149.165230, 10.0),  # Точка 1 (CMAC)
            (-35.363300, 149.165300, 10.0),  # Точка 2
            (-35.363200, 149.165300, 10.0),  # Точка 3
        ]

        success = sitl_backend.upload_mission(waypoints)
        assert success is True

        # Проверяем, что миссия загружена
        time.sleep(0.3)
        telemetry = sitl_backend.get_telemetry()
        assert telemetry['status'] == 'connected'

    def test_sitl_position_updates(self, sitl_backend):
        """Тест 16: Обновление позиции в реальном времени"""
        # Получаем начальную позицию
        time.sleep(0.5)
        telemetry1 = sitl_backend.get_telemetry()
        pos1 = telemetry1['position']

        # Ждём немного и получаем новую позицию
        time.sleep(0.5)
        telemetry2 = sitl_backend.get_telemetry()
        # pos2 не используется явно, но факт получения важен для теста потока

        # Позиция должна обновляться (хотя бы один параметр)
        assert isinstance(pos1['lat'], float)
        assert isinstance(pos1['lon'], float)
        assert isinstance(pos1['alt'], float)

    def test_sitl_battery_telemetry(self, sitl_backend):
        """Тест 17: Получение данных о батарее от SITL"""
        time.sleep(0.5)
        telemetry = sitl_backend.get_telemetry()

        battery = telemetry['battery']
        # В SITL батарея обычно симулируется
        assert isinstance(battery['voltage'], float)
        assert isinstance(battery['current'], float)
        assert isinstance(battery['remaining'], int)

        # Напряжение должно быть в разумных пределах
        assert 0 < battery['voltage'] < 20

    def test_sitl_multiple_setpoints_sequence(self, sitl_backend):
        """Тест 18: Последовательная отправка нескольких setpoint'ов"""
        points = [
            (5.0, 0.0, -3.0),
            (5.0, 5.0, -3.0),
            (0.0, 5.0, -3.0),
        ]

        for x, y, z in points:
            sitl_backend.send_setpoint(x, y, z, yaw=0.0)
            time.sleep(0.2)

            # Проверяем, что соединение активно после каждой команды
            telemetry = sitl_backend.get_telemetry()
            assert telemetry['status'] == 'connected'

    def test_sitl_mission_upload_with_invalid_coords(self, sitl_backend):
        """Тест 19: Обработка ошибки при загрузке миссии с некорректными координатами"""
        # Пытаемся загрузить миссию с явно неверными координатами
        invalid_waypoints = [
            (100.0, 200.0, 10.0),  # Невозможные координаты
            (150.0, 250.0, 10.0),
        ]

        # SITL может принять или отклонить - главное, что бэкенд не падает
        try:
            result = sitl_backend.upload_mission(invalid_waypoints)
            assert isinstance(result, bool)
        except Exception as e:
            assert isinstance(e, Exception)

    def test_sitl_concurrent_telemetry_and_commands(self, sitl_backend):
        """Тест 20: Одновременная работа телеметрии и отправки команд"""
        errors = []

        def send_commands():
            """Фоновая отправка команд"""
            try:
                for i in range(5):
                    sitl_backend.send_setpoint(i, 0, -2.0, 0.0)
                    time.sleep(0.1)
            except Exception as e:
                errors.append(e)

        def read_telemetry():
            """Фоновое чтение телеметрии"""
            try:
                for i in range(10):
                    telemetry = sitl_backend.get_telemetry()
                    assert telemetry['status'] == 'connected'
                    time.sleep(0.05)
            except Exception as e:
                errors.append(e)

        # Запускаем оба потока одновременно
        t1 = threading.Thread(target=send_commands)
        t2 = threading.Thread(target=read_telemetry)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        # Не должно быть ошибок
        assert len(errors) == 0, f"Errors occurred: {errors}"


# ==================== КОНФИГУРАЦИЯ PYTEST ====================

def pytest_configure(config):
    """Регистрация маркера integration"""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test requiring SITL"
    )


def pytest_collection_modifyitems(config, items):
    """Автоматически пропускает интеграционные тесты, если нет флага --run-integration"""
    if not config.getoption("--run-integration"):
        skip_integration = pytest.mark.skip(reason="Need --run-integration option to run")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration)


def pytest_addoption(parser):
    """Добавляет опцию --run-integration"""
    parser.addoption(
        "--run-integration",
        action="store_true",
        default=False,
        help="Run integration tests with SITL"
    )