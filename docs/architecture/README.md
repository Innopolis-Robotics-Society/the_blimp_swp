# Architecture Documentation

This document describes the architecture of the Autonomous Indoor Airship Simulation system.

## Overview

The system consists of:
- **ArduPilot SITL** – simulation environment (from `ardupilot-for-custom-blimp`)
- **MAVLink Backend** – REST API + MAVLink communication (in `mavlink_backend/`)
- **QGroundControl** – ground station for monitoring and control
- **Python scripts** – mission upload, telemetry processing

## Static View

The component diagram shows the main system components and their interactions.

[Component diagram](static-view/component-diagram.png)

**PlantUML source:** [component-diagram.puml](static-view/component-diagram.puml)

### Coupling and Cohesion
- The backend communicates with SITL via MAVLink over UDP.
- QGroundControl is used as a separate tool, not integrated into our code.
- The backend provides REST API and WebSocket for telemetry.

### Maintainability
- The system is modular: backend, SITL, and scripts are separate.
- MAVLink abstraction makes it possible to switch hardware later.

### Quality Requirements Support
- QR-01 (MAVLink speed) is implemented in the backend.
- QR-02 (SITL stability) depends on the SITL environment.
- QR-03 (Telemetry rate) is handled by the backend streaming.

---

## Dynamic View

The sequence diagram shows the mission upload flow.

[Sequence diagram](dynamic-view/sequence-diagram.png)

**PlantUML source:** [sequence-diagram.puml](dynamic-view/sequence-diagram.puml)

### Scenario
This diagram shows how a user uploads a mission via the backend.

### Why it matters
This flow is critical for autonomous flight and shows the interaction between components.

### Quality Requirements
- QR-01 (speed) is tested during mission upload.
- QR-03 (telemetry) is updated during this flow.

---

## Deployment View

The deployment diagram shows where components run.

[Deployment diagram](deployment-view/deployment-diagram.png)

**PlantUML source:** [deployment-diagram.puml](deployment-view/deployment-diagram.puml)

### Deployment model
- SITL runs in Docker (locally).
- Backend runs locally (or on Raspberry Pi).
- QGroundControl runs on the user's machine.
- MAVLink communication happens over UDP.

### Why this model
- Simple for development and testing.
- Can be moved to hardware when available.

### Constraints
- Requires Docker and Python.
- No hardware yet — we use SITL.

---

## Architecture Decision Records (ADRs)

- [ADR-001: Use ArduPilot SITL for simulation](adr/ADR-001-use-ardupilot-sitl.md)
- [ADR-002: Use MAVLink for communication](adr/ADR-002-use-mavlink.md)
- [ADR-003: Use Python for backend](adr/ADR-003-use-python-backend.md)
