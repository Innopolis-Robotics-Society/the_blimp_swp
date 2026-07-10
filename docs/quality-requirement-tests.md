# Quality Requirements and Tests

## QR-01: MAVLink message speed

**ISO/IEC 25010 sub-characteristic:** Performance Efficiency — Time Behaviour  
**Why it matters:** The system must process MAVLink messages fast enough to keep the airship stable and show telemetry in real time.  
**What we check:** When the system gets a MAVLink heartbeat, it must parse and save it within **50 ms** on a Raspberry Pi 4 (or similar hardware).  
**How we test:** QRT-01 runs automatically in CI. It sends 100 messages and checks the average time. If it is over 50 ms, the test fails.  
**Related stories:** US-12, US-15, US-21.

---

## QRT-01: MAVLink message speed test

**Quality Requirement:** QR-01  
**Type:** Automated CI test (Python)  
**Location:** `tests/test_mavlink_performance.py`  
**What it does:** Sends 100 MAVLink heartbeat messages and measures the average processing time.  
**Pass condition:** Average time ≤ 50 ms.

```python
# tests/test_mavlink_performance.py
import time
import random
# Example implementation

def test_mavlink_processing_time():
    times = []
    for _ in range(100):
        message = {
            'type': 'HEARTBEAT',
            'system_id': random.randint(1, 255),
            'component_id': 1,
            'sequence': random.randint(0, 255)
        }
        start = time.time()
        process_heartbeat(message)
        times.append(time.time() - start)
    avg = sum(times) / len(times)
    assert avg <= 0.05, f"Average time {avg:.3f}s is too slow (must be ≤ 0.05s)"
```
## QR-02: SITL stability
**ISO/IEC 25010 sub-characteristic:** Reliability — Maturity
**Why it matters:** The simulation must not crash during tests or demos.
**What we check:** The system runs a 5-minute mission with at least 3 waypoints and MAVLink connection. No crashes or errors are allowed.
**How we test:** QRT-02 runs this mission in CI. If the simulation crashes or shows an error, the test fails.
**Related stories:** US-12, US-13, US-21.
**QRT-02: SITL stability test**
**Quality Requirement:** QR-02
**Type:** Automated CI test (Python + SITL)
**Location:** tests/test_sitl_stability.py
**Description:** Launches SITL, uploads a 3-waypoint mission, and runs for 5 minutes. Checks for crashes or critical errors.
**Pass criteria:** No crash or error during the 5-minute run.

```python
# tests/test_sitl_stability.py
# Example implementation
import subprocess
import time

def test_sitl_stability():
    sitl = subprocess.Popen(
        ["sim_vehicle.py", "-v", "ArduCopter", "--console", "--map"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(300)
    assert sitl.poll() is None, "SITL crashed or stopped during the test"
    sitl.terminate()
    sitl.wait(timeout=10)
```
## QR-03: Telemetry update rate
**ISO/IEC 25010 sub-characteristic:** Performance Efficiency — Resource Utilization
**Why it matters:** Telemetry must update often enough for safe manual control and good logging.
**What we check:** The system must send telemetry (position, attitude, velocity) at least 10 times per second during simulation.
**How we test:** QRT-03 checks the telemetry stream. If the average rate is below 10 Hz, the test fails.
**Related stories:** US-15.
**QRT-03: Telemetry update rate test**
**Quality Requirement:** QR-03
**Type:** Automated CI test (Python)
**Location:** tests/test_telemetry_rate.py
**Description:** Listens for telemetry messages and counts updates over 10 seconds.
**Pass criteria:** Telemetry updates at least 10 times per second.

```python
# tests/test_telemetry_rate.py
import time
# Example implementation

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
