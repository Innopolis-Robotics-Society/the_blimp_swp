# Week 4 Reflection

## What we learned
- We learned how to write quality requirements (speed, stability, telemetry rate) and turn them into automated tests.
- We learned that customer feedback should guide the next Sprint — we listened to his approval of Python and his request to put QGC in Docker.
- We saw that quality and automation take time and may reduce the number of features, but they make the product more reliable.

## What we confirmed
- Python simulator is enough → **Yes** (customer said no Unity).
- We need a separate GUI → **No** (customer said MAVLink + QGC is fine).
- Hardware would be ready → **No** (still not available, we use SITL).

## Problems we faced
- No hardware for testing (UWB, real flight controller).
- US-14 (UWB) and US-22 (smoke-check) are not finished.
- We had no tests before — we started from zero.

## What we will do next
- Next Sprint: finish UWB and smoke-check.
- Add tests for all new code.
- Keep using SITL — don't wait for hardware.
- Keep quality requirements and tests as part of the Definition of Done.
