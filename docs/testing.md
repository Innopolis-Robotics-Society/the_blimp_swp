# Testing Strategy

## Test levels

### Unit tests
We test critical functions in Python (MAVLink processing, telemetry handling, mission upload).  
Location: `tests/unit/`

### Integration tests
We test connections between components: SITL ↔ backend, MAVLink ↔ QGroundControl.  
Location: `tests/integration/`

### Quality requirement tests (QRT)
Automated tests for quality requirements (QR-01, QR-02, QR-03).  
Location: `tests/`

## Critical modules
- MAVLink message processing
- Telemetry streaming
- Mission upload
- SITL startup and stability

## Coverage
We require at least **30% line coverage** for critical modules.  
We track coverage using `pytest-cov`.

## CI
All tests run on GitHub Actions on every push to `main` and on pull requests.

## Additional QA checks
- We use `pytest` for test discovery and execution.
- We use `pylint` for static code analysis.
- Link checking (Lychee) is already configured and runs in CI.

## Test execution
**Run all tests locally:**
```bash
pytest tests/
**Run with coverage:**
```bash
pytest --cov=. tests/
```
---

**MVP v2 updates**
- Added UAT-04 and UAT-05 scenarios.
- Custom ArduPilot vehicle (ArduMotorBlimp) build is tested in CI.
- Dockerized SITL is verified on Linux.
