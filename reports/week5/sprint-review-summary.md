# Sprint Review Summary

**Date:** 05.07.2026
**Participants:**
- Daniyar (Product Owner)
- Arina (Scrum Master)
- Iuliana (Developer)
- Svetlana (Developer)
- Eugene (Customer)

---

## Sprint Goal reviewed
Deliver MVP v2 with architecture documentation and ADRs.

## Delivered increment

- MVP v2 implementation completed
- Architecture documentation (static, dynamic, and deployment views)
- Three Architecture Decision Records (ADRs)
- Development process documentation
- Two additional UAT scenarios
- Release v0.3.0

## UAT results
- UAT-01: SITL started, heartbeat received – passed
- UAT-02: Mission uploaded, vehicle moved – passed
- UAT-03: Telemetry visible in QGroundControl – passed

## Customer feedback
- Dockerized SITL environment works.
- Customer suggested removing Windows support from documentation to simplify setup.
- Customer confirmed that ArduPilot Blimp modifications are needed.
- Customer asked to coordinate with Egor (Capstone team) on vehicle configuration.

## Decisions
- Continue with custom ArduPilot Blimp vehicle (ArduMotorBlimp).
- Remove Windows instructions from documentation.
- Coordinate with Capstone team on motor frames and build issues.

## Action points
- Finish MVP v2 implementation.
- Complete architecture diagrams (PlantUML).
- Create release v0.3.0.
- Record public demo video.
