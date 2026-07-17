# Roadmap

This document describes the final roadmap and completion state of the SWP course project.

**Last updated:** 17 July 2026

---

## Course Outcome Goal

Deliver a customer-usable simulation environment for an autonomous indoor airship, complete the customer handover process, and finalize the Software Engineering project with a stable MVP release and full documentation.

---

## Completed Milestones

### Sprint 1 (Week 1-2) - Project Initialization
- [x] Team formation and role assignment
- [x] Initial customer meeting and requirements gathering
- [x] Product Backlog and first user stories
- [x] Repository setup with CI, documentation, and license
- [x] **Release:** v0.1.0

### Sprint 2 (Week 3-4) - Core Architecture
- [x] Architecture documentation and ADRs
- [x] Initial project structure (`mavlink_backend/`, `sitl/`, `docs/`)
- [x] Basic documentation suite
- [x] **Release:** v0.2.0

### Sprint 3 (Week 5) - MVP v2
- [x] ArduPilot SITL Docker integration
- [x] Initial MAVLink backend (Python scripts)
- [x] Customer handover documentation (initial version)
- [x] UAT scenarios defined
- [x] **Release:** v0.3.0 - **MVP v2**

### Sprint 4 (Week 6) - Trial Release & Transition Readiness
- [x] QGroundControl Docker integration
- [x] MAVLink backend restructured as Python package with FastAPI
- [x] Comprehensive test suite for backend (~83% coverage)
- [x] `CONTRIBUTING.md` and `AGENTS.md` created/updated
- [x] `docs/customer-handover.md` updated with current state
- [x] Trial release created
- [x] **Release:** v0.4.0 - **Trial Release**

---

## Final Milestone

### Sprint 5 (Week 7) – Final Delivery (MVP v3)

**Status: Completed**

### Sprint Goal

Deliver the final MVP, complete customer handover, finalize documentation, and successfully conclude the Software Engineering project.

### Completed Deliverables

- [x] Customer handover completed
- [x] Final Sprint Review completed
- [x] Customer acceptance confirmed
- [x] Final documentation completed
- [x] Final release v0.5.0 published

### Release

**v0.5.0 – Final MVP**

---

## Project Status

The Software Engineering project has been successfully completed.

The repository now contains the final accepted version of the Autonomous Indoor Airship Simulation project.

Future development, maintenance, and hardware extensions may be carried out by the Innopolis Robotics Lab independently of the Software Engineering course.

---

## Future Development

Possible future improvements include:

- advanced autonomous navigation;
- additional onboard sensors;
- localization improvements;
- hardware-specific extensions.

These activities are outside the scope of the completed Software Engineering course project.

---

## GitHub Milestones

The project progress was tracked through GitHub Milestones:

- [Sprint 1 - Project Initialization](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/1)
- [Sprint 2 - Core Architecture](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/2)
- [Sprint 3 - MVP v2](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/3)
- [Sprint 4 - Trial Release & Transition Readiness](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/4)
- [Sprint 5 - Final Delivery (MVP v3)](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/5)

---

## Related Artifacts

- [Customer Handover](./customer-handover.md)
- [CHANGELOG.md](../CHANGELOG.md)
- [Product Backlog](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues)
