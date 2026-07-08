# ADR-002: Use MAVLink for communication

## Status
Accepted

## Context
We need a communication protocol between the backend, SITL, and ground station. The protocol must support telemetry, mission upload, and command sending.

## Decision
We use MAVLink protocol version 2.

## Rationale
- Standard protocol for ArduPilot.
- Supports heartbeat, telemetry, mission upload.
- Works over UDP.
- Supported by QGroundControl.

## Consequences
- We must implement MAVLink message handling.
- We rely on `pymavlink` library.

## Related Quality Requirements
- QR-01: MAVLink message speed
- QR-03: Telemetry rate
