import pytest
from unittest.mock import Mock, patch


@pytest.fixture
def mock_master():
    master = Mock()
    master.target_system = 1
    master.target_component = 1
    return master


@pytest.fixture
def backend(mock_master):
    from mavlink_backend import MAVLinkBackend

    with patch('mavlink_backend.backend.mavutil.mavlink_connection', return_value=mock_master):
        with patch.object(mock_master, 'wait_heartbeat'):
            b = MAVLinkBackend(connection_string='udp:test')
            b.stop()
            yield b


@pytest.fixture
def sitl_backend():
    from mavlink_backend import MAVLinkBackend

    try:
        backend = MAVLinkBackend('udp:127.0.0.1:14550')
        yield backend
        backend.stop()
    except Exception as e:
        pytest.skip(f"SITL not available or connection failed: {e}")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "integration: mark test as integration test requiring SITL"
    )


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-integration"):
        skip_integration = pytest.mark.skip(reason="Need --run-integration option to run")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration)


def pytest_addoption(parser):
    parser.addoption(
        "--run-integration",
        action="store_true",
        default=False,
        help="Run integration tests with SITL"
    )
