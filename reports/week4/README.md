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
- [CI Pipeline](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/actions)

---

## Sprint Goal
Improve product quality with automated tests, quality requirements, and CI checks.

## Sprint Dates
Start: 23 June 2026  
Finish: 28 June 2026

## Sprint Scope
- [x] Add quality requirements and tests 
- [x] Update Definition of Done
- [x] Create UAT scenarios
- [x] Customer review

## Total Story Points
Sprint total: 26

---

## Customer Feedback Response Table

| Feedback point | Resulting PBI or issue | Status | Response |
|---|---|---|---|
| Customer said Python simulator is enough, no Unity needed. | — | Done | We keep Python. |
| Customer wants QGroundControl in Docker. | [#3](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues/3) | Planned | Will be added in the next Sprint. |
| Customer wants to see the simulator. | [#34](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues/34) | Done | Documentation and demo provided. |

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
- Automated tests for quality requirements are added.
- Tests run in CI on every push.
- Critical modules have at least 30% line coverage.

---

## Status
- [x] Quality requirements: done
- [x] Quality requirement tests: done
- [x] Definition of Done: updated
- [x] UAT scenarios: ready and passed with customer
- [x] Customer meeting: done on 28.06.2026
- [x] Release v0.2.0: [created](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.2.0)
- [x] All Sprint issues: closed

---

## Demo Video
[Watch the demo on Yandex Disk](https://disk.yandex.ru/i/Euiq1Bod1XcbEg)

---

## Next Steps
- Start work on UWB and smoke-check in the next Sprint
- Coordinate with Capstone team on motor frames
- Prepare for Assignment 5

---

## Documents
- [Reflection](reflection.md)
- [Retrospective](retrospective.md)
- [LLM Report](llm-report.md)
- [Customer Review Summary](customer-review-summary.md)
- [Customer Review Transcript](customer-review-transcript.md)
