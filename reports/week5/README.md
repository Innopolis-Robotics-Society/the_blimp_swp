# Week 5 Report

## Project Information
**Project name:** Autonomous Indoor Airship Simulation  
**License:** [MIT License](../../LICENSE)

---

## Links
- [Product Backlog](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues)
- [Sprint Backlog](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/3)
- [Sprint Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/3)
- [Roadmap](../../docs/roadmap.md)
- [Definition of Done](../../docs/definition-of-done.md)
- [Quality Requirements](../../docs/quality-requirements.md)
- [Quality Requirement Tests](../../docs/quality-requirement-tests.md)
- [Testing](../../docs/testing.md)
- [User Acceptance Tests](../../docs/user-acceptance-tests.md)
- [Development Process](../../docs/development-process.md)
- [Architecture](../../docs/architecture/README.md)
- [ADRs](../../docs/architecture/adr/)
- [CHANGELOG](../../CHANGELOG.md)
- [CI Pipeline](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/actions)
- [Hosted Documentation](https://innopolis-robotics-society.github.io/the_blimp_swp/)

---

## Sprint Goal
Deliver MVP v2 with architecture documentation and ADRs.

## Sprint Dates
Start: 01 July 2026  
Finish: 05 July 2026

## Sprint Scope
- [x] Architecture documentation (static, dynamic, deployment views)
- [x] 3 ADRs
- [x] Development process documentation
- [x] MVP v2 implementation
- [x] 2 new UAT scenarios
- [x] Release v0.3.0

## Sprint Review
- [Recording](https://disk.yandex.ru/i/eWTmeSGCYJ8JZw)
- [Demo video](https://disk.yandex.ru/i/Gnx4jJR4zkuf9Q)
- [Transcript](sprint-review-transcript.md)
- [Summary](sprint-review-summary.md)

## Total Story Points
Sprint total: 26

---

## Customer Feedback Response Table

| Feedback point | Resulting PBI or issue | Status | Response |
|---|---|---|---|
| Customer wants QGroundControl in Docker. | [#3](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues/3) | Done | Added to Docker setup. |
| Customer asked for documentation automation. | [#42](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues/42) | Done | Added ADRs and architecture docs. |
| Customer suggested removing Windows support from docs. | [#52](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/pull/52) | Done | Removed Windows instructions from README. |

---

## Contribution traceability

| Name | Issues | PRs | Reviews | Other |
|------|--------|-----|---------|-------|
| Daniyar (DaniK-51) | #3, #48 | #50 | #45, #46, #47, #49, #50, #52 | Sprint Review, ArduPilot config, team coordination |
| Arina (mimics0s) | #42 | #45, #52 | — | Docs, ADRs, reports, PDF, root README |
| Iuliana (kaftanovaa) | #40 | — | — | Backend tests, MAVLink |
| Svetlana (withearrt) | #47, #48, #49 | #46, #50 | — | Diagrams, UAT, Docker, QGC in Docker |

---

## Architecture Summary

The system architecture is documented using three complementary views:

- [**Static view (component diagram):**](../../docs/architecture/static-view/static-view.png) — describes the main software components and their relationships.
- [**Dynamic view (sequence diagram):**](../../docs/architecture/dynamic-view/dynamic-view.png) — illustrates the mission upload workflow and interactions between system components.
- [**Deployment view (deployment diagram):**](../../docs/architecture/deployment-view/deployment-view.png) — shows how the backend, SITL, and QGroundControl are deployed and communicate.

The complete architecture documentation is available in
[Architecture Documentation](../../docs/architecture/README.md), together with the corresponding Architecture Decision Records (ADRs).

## Testing and CI Status
- Tests pass in CI.
- Coverage target (30% for critical modules) is satisfied.
- Quality requirement tests are passing.

---

## Status
- [x] Architecture docs: done
- [x] ADRs: done
- [x] MVP v2: done
- [x] UAT: done

---

## Next Steps
- Prepare for Assignment 6
- Start integration with Capstone team on motor frames

## Documents
- [Reflection](reflection.md)
- [Retrospective](retrospective.md)
- [LLM Report](llm-report.md)
- [Sprint Review Summary](sprint-review-summary.md)
- [Sprint Review Transcript](sprint-review-transcript.md)
