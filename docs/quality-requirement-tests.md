# Quality Requirement Tests

## QRT-01: MAVLink message speed

**Quality Requirement:** QR-01  
**Type:** Automated CI test (Python)  
**Location:** `tests/test_mavlink_performance.py`  
**What it does:** Sends 100 MAVLink heartbeat messages and measures the average processing time.  
**Pass condition:** Average time ≤ 50 ms.

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
    avg = sum(times) / len(times)
    assert avg <= 0.05, f"Average time {avg:.3f}s is too slow"
