# Week 7 Report

This directory contains the documentation produced during the final sprint of the Software Engineering project.

Sprint 5 concluded the development of the **Autonomous Indoor Airship Simulation** project. During this sprint, the team completed remaining implementation tasks, finalized documentation, performed final transition activities, demonstrated the system to the customer, and delivered the final MVP v3 release.

---

# Sprint Information

| Item | Value |
|------|-------|
| Sprint | Sprint 5 |
| Sprint Dates | 13.07.2026 - 19.07.2026 |
| Duration | Week 7 |
| Release | v0.5.0 (MVP v3) |
| Customer | Eugene Shlomov (Innopolis Robotics Lab) |
| Sprint Goal | Deliver MVP v3, complete final transition, finalize documentation, and prepare the project for customer maintenance. |

---

# Project Management Links

- [Product Backlog:](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues)

- [Sprint 5 Backlog, Sprint 5 Milestone:](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/5?closed=1)

- Previous Sprint Report:
  [Week 6 Report](../week6/README.md)
  
- [Hosted Documentation](https://innopolis-robotics-society.github.io/the_blimp_swp/)

---

# Sprint Outcome

The Sprint 5 goal was successfully achieved.

During the final sprint the team:

- completed the remaining implementation tasks;
- deployed the customized firmware;
- verified MAVLink communication between the backend, flight controller, and ground station;
- finalized project documentation;
- completed customer handover activities;
- delivered the final MVP v3 release;
- prepared final Demo Day materials.

The customer accepted the delivered project following the final Sprint Review.

---

# Sprint Backlog

All Sprint 5 Product Backlog Items were completed before the final delivery.

| Issue | Description | Status |
|------|-------------|--------|
| [#25 Create one-click launch script](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues/25) | Provide a single command workflow for starting SITL and backend services | Closed |
| [#12 Create physical engine for SITL](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues/12) | Implement custom Python-based physical simulation engine | Closed |
| [#6 Test RPI-to-FC connection](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues/6) | Validate MAVLink communication chain between Raspberry Pi and Flight Controller | Closed |
| [#5 Configure ArduPilot for a Blimp](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues/5) | Customize ArduPilot configuration for the blimp platform | Closed |

---

## Sprint Size

Total Sprint 5 size: 20 Story Points

---

# Technical Achievements

The following achievements were completed during Sprint 5:

- Final project release v0.5.0 (MVP v3)
- Customized ArduPilot firmware integration
- MAVLink communication verification
- Physical hardware validation
- One-click SITL launch workflow
- Final repository documentation update
- Customer handover preparation

---

# Final Transition Outcome

## Handover Level

Reached handover level:

**Ready for independent use**

The final repository contains the required source code, setup instructions, operational documentation, and customer handover materials required for future maintenance.

## Customer Confirmation Status

**Accepted**

The customer confirmed that the delivered functionality and documentation satisfied the agreed project scope.

## Transition Summary

The following project assets were transferred:

- source repository;
- Docker-based SITL environment;
- customized ArduPilot firmware;
- MAVLink backend implementation;
- project documentation;
- customer handover documentation.

Detailed transition information is available in:

[Customer Handover Documentation](../../docs/customer-handover.md)

---

# Customer Review

The final Sprint Review included a demonstration of the completed system and a walkthrough of the repository.

The customer confirmed that:

- the agreed project objectives had been achieved;
- the delivered functionality satisfied the agreed scope;
- the documentation was sufficient for future maintenance;
- the repository contained the required deliverables.

The project was accepted without critical issues.

---

# UAT Summary

Relevant user acceptance scenarios were reviewed during final validation.

| Scenario | Result |
|-----------|--------|
| Start simulation environment | Passed |
| Launch MAVLink backend | Passed |
| Establish communication with flight controller | Passed |
| Connect QGroundControl | Passed |
| Verify documented setup procedure | Passed |

No critical UAT failures remained before final delivery.

---

# Final Review Follow-up

| Review Item | Action Taken | Status |
|-------------|--------------|--------|
| Documentation review | Updated project documentation and handover materials | Completed |
| Repository organization | Finalized repository structure and documentation links | Completed |
| MVP validation | Verified final MVP v3 workflow | Completed |

---

# Team Contributions

| Team Member | Contribution |
|-------------|--------------|
| Daniyar | Product Owner responsibilities, ArduPilot customization, release management, customer communication |
| Arina | Documentation, customer handover, sprint reports, final repository preparation |
| Iuliana | MAVLink communication testing, hardware validation |
| Svetlana | Firmware deployment, Docker environment, demonstration preparation |

---

# Contribution Traceability

| Team Member | Issues / Activities |
|-------------|---------------------|
| Daniyar | #5 ArduPilot customization, release preparation, customer communication |
| Arina | Documentation updates, handover documentation, repository preparation |
| Iuliana | #6 MAVLink communication validation and testing |
| Svetlana | Firmware deployment, SITL environment preparation |

---

# Final Deliverables

The final project delivery includes:

- source code;
- Docker-based SITL environment;
- customized ArduPilot firmware;
- FastAPI MAVLink backend;
- QGroundControl integration;
- project documentation;
- architecture documentation;
- quality assurance documentation;
- sprint documentation;
- customer handover documentation.

---

# Final Release

## v0.5.0 - Final MVP (MVP v3)

The final release includes:

- completed simulation environment;
- Docker-based SITL workflow;
- FastAPI MAVLink backend;
- QGroundControl integration;
- customized ArduPilot configuration;
- final documentation package.

Release:

https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.5.0

---

# Public Demo Video

Final sanitized MVP v3 demonstration video:

https://disk.yandex.ru/i/QiNKBpdfEEh6EQ

---

# Final Product Access

The final product and documentation can be accessed using:

- [Hosted Documentation](https://innopolis-robotics-society.github.io/the_blimp_swp/)
- [v0.5.0 MVP v3 Release](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.5.0)
- [Run Instructions](../../README.md)
- [Customer Handover Documentation](../../docs/customer-handover.md)

---

# Demo Day Preparation

The team completed the required Week 7 rehearsal preparation.

Preparation included:

- final presentation structure;
- product demonstration preparation;
- review of project contributions;
- preparation of MVP v3 explanation;
- preparation of remaining limitations and future work discussion.

---

# Repository Status

At the completion of Sprint 5, the repository represents the final accepted state of the Software Engineering project.

All planned Sprint 5 Product Backlog Items have been completed, the final release v0.5.0 has been delivered, and the project has been accepted by the customer.

The repository now serves as the primary source of documentation and implementation for future maintenance and development.

---

# Related Documents

| Document | Description |
|----------|-------------|
| [Customer Handover](../../docs/customer-handover.md) | Final project handover documentation |
| [Sprint Review Summary](sprint-review-summary.md) | Summary of final Sprint Review |
| [Sprint Review Transcript](sprint-review-transcript.md) | Sprint Review transcript |
| [Reflection](reflection.md) | Sprint reflection |
| [Retrospective](retrospective.md) | Sprint retrospective |
| [LLM Usage Report](llm-report.md) | LLM usage documentation |
| [Roadmap](../../docs/roadmap.md) | Project timeline and milestones |
| [CHANGELOG](../../CHANGELOG.md) | Release history |
| [README](../../README.md) | Repository entry point |
| [CONTRIBUTING](../../CONTRIBUTING.md) | Contribution guidelines |
| [AGENTS](../../AGENTS.md) | Agent development guidance |
| [Week 6 Report](../week6/README.md) | Sprint 4 final report and trial release evidence |

---

# Remaining Limitations

The final MVP v3 has no blocking transition issues.

Known limitations:

- The system remains a simulation-focused environment.
- Physical deployment depends on available airship hardware.
- Further autonomous flight features may require additional development.

---

# Conclusion

Sprint 5 completed the development of the Autonomous Indoor Airship Simulation project.

The final MVP v3 release was delivered, the customer accepted the project, and all required Software Engineering course deliverables were completed.
