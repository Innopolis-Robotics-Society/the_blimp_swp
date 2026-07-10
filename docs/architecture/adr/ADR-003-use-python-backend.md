# ADR-003: Use Python for backend

## Status
Accepted

## Context
We need a backend to handle MAVLink communication and provide REST API and WebSocket for telemetry.

## Decision
We use Python with FastAPI.

## Rationale
- FastAPI is fast and easy to use.
- Python has good MAVLink support (`pymavlink`).
- The team is familiar with Python.
- Easy to run in Docker.

## Consequences
- We must maintain Python dependencies.
- Performance is acceptable for this use case.

## Related Quality Requirements
- QR-01: MAVLink message speed
- QR-03: Telemetry rate
