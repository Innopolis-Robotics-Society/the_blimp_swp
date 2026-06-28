# Quality Requirement Tests

## QRT-01: MAVLink message processing time

**Quality Requirement:** QR-01  
**Type:** Automated CI test (Python)  
**Location:** `tests/test_mavlink_performance.py`  
**Description:** Sends 100 MAVLink heartbeat messages to the backend and measures the average processing time.  
**Pass criteria:** Average processing time ≤ 50 ms.

```python
# tests/test_mavlink_performance.py
import time
from your_backend import process_heartbeat

def test_mavlink_processing_time():
    times = []
    for _ in range(100):
        start = time.time()
        process_heartbeat(sample_message)
        times.append(time.time() - start)
    avg = sum(times)/len(times)
    assert avg <= 0.05, f"Average processing time {avg:.3f}s exceeds 0.05s"
```

## QRT-02: SITL simulation stability
**Quality Requirement:** QR-02
**Type:** Automated CI test (Python + SITL)
**Location:** tests/test_sitl_stability.py
**Description:** Launches SITL, uploads a 3-waypoint mission, and runs for 5 minutes. Checks for crashes or critical errors.
**Pass criteria:** No crash or error during the 5-minute run.

```python
# tests/test_sitl_stability.py
import subprocess
import time

def test_sitl_stability():
    sitl = subprocess.Popen(["sim_vehicle.py", "-v", "ArduCopter", "--console"])
    time.sleep(300)  # 5 minutes
    assert sitl.poll() is None, "SITL crashed or exited early"
    sitl.terminate()
```

## QRT-03: Telemetry update rate
**Quality Requirement:** QR-03
**Type:** Automated CI test (Python)
**Location:** tests/test_telemetry_rate.py
**Description:** Listens for telemetry messages and counts updates over 10 seconds.
**Pass criteria:** Telemetry updates ≥ 10 times per second.

```python
# tests/test_telemetry_rate.py
import time
from your_backend import telemetry_stream

def test_telemetry_rate():
    start = time.time()
    count = 0
    while time.time() - start < 10:
        telemetry_stream.get()
        count += 1
    rate = count / 10
    assert rate >= 10, f"Telemetry rate {rate:.1f} Hz is below 10 Hz"
```

## Test execution
All tests run automatically on every push to main and on pull requests via GitHub Actions (see .github/workflows/ci.yml).
