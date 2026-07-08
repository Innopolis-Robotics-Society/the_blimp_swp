# ADR-001: Use ArduPilot SITL for simulation

## Status
Accepted

## Context
We need a simulation environment to test the airship autopilot without real hardware. The simulation must support MAVLink and custom vehicle types.

## Decision
We use ArduPilot SITL (Software-in-the-Loop) with Blimp support, based on the `ardupilot-for-custom-blimp` repository.

## Rationale
- Open source and well-documented.
- Supports MAVLink out of the box.
- Already used by the customer.
- Allows custom vehicle configuration for near-zero buoyancy.

## Consequences
- We need to configure SITL for Blimp.
- We rely on an external repository.

## Related Quality Requirements
- QR-02: SITL stability
- QR-03: Telemetry rate
