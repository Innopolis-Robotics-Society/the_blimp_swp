# Roadmap

This document describes the project roadmap through the end of the SWP course. It does not extend into speculative post-course version planning.

**Last updated:** 12 July 2026

---

## Course Outcome Goal

Deliver a customer-usable simulation environment for an autonomous indoor airship, transitioned to the Innopolis Robotics Lab with complete documentation and a stable release.

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

---

## Current Milestone

### Sprint 4 (Week 6) - Trial Release & Transition Readiness
- [x] QGroundControl Docker integration
- [x] MAVLink backend restructured as Python package with FastAPI
- [x] Comprehensive test suite for backend (~83% coverage)
- [x] `CONTRIBUTING.md` and `AGENTS.md` created/updated
- [x] `docs/customer-handover.md` updated with current state
- [x] Trial release v0.4.0 created
- [ ] Customer meeting (blocked - customer unavailable; rescheduled to Week 7)
- **Release:** v0.4.0 - **Trial Release**

---

## Upcoming Milestones

### Sprint 5 (Week 7) - Final Delivery (MVP v3)
- [ ] Conduct customer meeting and collect trial feedback
- [ ] Execute UAT with customer
- [ ] Address customer-reported issues
- [ ] Finalize transition documentation
- [ ] Confirm handover level with customer
- [ ] Prepare Demo Day presentation and demo video
- [ ] **Release:** v0.5.0 - **MVP v3 (final course version)**

### Week 8 - Demo Day
- [ ] Lab rehearsal presentation (Week 7)
- [ ] Final Demo Day presentation
- [ ] Course completion

---

## Post-Course State

At course completion, the project will be in one of the following handover states (see [docs/customer-handover.md](./customer-handover.md)):

- **Ready for independent use** - documentation and setup are sufficient for the customer to operate the product without team support
- **Independently used by customer** - customer has validated the product in their environment
- **Deployed or operated on customer side** - product is running in the customer's infrastructure

The Lab team will take over maintenance, future feature development, and any hardware integration work after course completion.

---

## Out of Scope (Post-Course)

The following items are explicitly out of scope for the course and will be addressed by the Lab team after handover:

- Physical flight controller integration
- UWB localization system integration
- Real sensor data processing (IMU, cameras)
- Production authentication and authorization
- Multi-vehicle coordination
- Performance optimization for production use

These items are documented in [docs/customer-handover.md](./customer-handover.md) as future work.

---

## Related Artifacts

- [Customer Handover](./customer-handover.md)
- [CHANGELOG.md](../CHANGELOG.md)
- [Week 6 Report](../reports/week6/README.md)
- [Product Backlog](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues)
