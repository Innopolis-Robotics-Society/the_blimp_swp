# Week 4 Report

## Project Information
**Project name:** Autonomous Indoor Airship Simulation  
**License:** [MIT License](../../LICENSE)

---

## Links
- [Product Backlog](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues)
- [Sprint Backlog](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/2)
- [Sprint Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/2)
- [Roadmap](../../docs/roadmap.md)
- [Definition of Done](../../docs/definition-of-done.md)
- [Quality Requirements](../../docs/quality-requirements.md)
- [Quality Requirement Tests](../../docs/quality-requirement-tests.md)
- [Testing](../../docs/testing.md)
- [User Acceptance Tests](../../docs/user-acceptance-tests.md)
- [CHANGELOG](../../CHANGELOG.md)
- [CI Pipeline](link-to-your-actions-run)

---

## Sprint Goal
Improve product quality with automated tests, quality requirements, and CI checks.

## Sprint Dates
Start: 23 June 2026  
Finish: 30 June 2026

## Sprint Scope
- Add quality requirements and tests
- Update Definition of Done
- Create UAT scenarios
- Prepare for customer review

## Total Story Points
Sprint total: (to be filled)

---

## Customer Feedback Response Table

| Feedback point | Resulting PBI or issue | Status | Response |
|---|---|---|---|
| Customer said Python simulator is enough, no Unity needed. | — | Done | We keep Python. |
| Customer wants QGroundControl in Docker. | [#3](link) | Planned | We will add it later. |
| Customer wants to see the simulator. | — | Done | Link sent after meeting. |

---

## Quality Requirements Summary

We use ISO/IEC 25010. Quality requirements are in `docs/quality-requirements.md`.

| ID | Sub-characteristic | Summary |
|---|---|---|
| QR-01 | Performance Efficiency — Time Behaviour | MAVLink messages processed in <50 ms |
| QR-02 | Reliability — Maturity | SITL runs 5 minutes without crash |
| QR-03 | Performance Efficiency — Resource Utilization | Telemetry sends at least 10 times per second |

---

## Testing Summary
- We added automated tests for quality requirements.
- Tests run in CI on every push.
- Critical modules have at least 30% line coverage.

---

## Status
- Quality requirements: done
- Quality requirement tests: done
- Definition of Done: updated
- UAT scenarios: ready
- Customer meeting: planned for Sunday

---

## Next Steps
- Run UAT with customer
- Record demo video
- Create release v0.2.0

---

## Documents
- [Reflection](reflection.md)
- [Retrospective](retrospective.md)
- [LLM Report](llm-report.md)
- [Customer Review Summary](customer-review-summary.md)
