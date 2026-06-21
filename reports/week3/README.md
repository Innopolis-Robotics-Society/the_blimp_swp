# Week 3 Report

## Project Information
**Project name:** Autonomous Indoor Airship Simulation  
**License:** [MIT License](../../LICENSE)

## Links
- [User stories (current)](../../docs/user-stories.md)
- [Historical user stories (Week 2)](../week2/user-stories.md)
- [Sprint Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/1)
- [Roadmap](../../docs/roadmap.md)
- [Definition of Done](../../docs/definition-of-done.md)
- [CHANGELOG](../../CHANGELOG.md)
- [Process Requirements](https://gitlab.pg.innopolis.university/swp_26/swp_26/-/blob/main/Process_Requirements.md#product-backlog-items-and-scope)

## Product Backlog
We do not use GitHub Projects. Instead, we track the Product Backlog using **open Issues**. All active user stories and tasks are stored as issues with labels for type and priority.

- All open issues: [Issues](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues)
- Filtered by user stories: [User stories](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues?q=is%3Aissue%20state%3Aopen%20label%3Auser-story)

## Sprint Backlog
We track the Sprint Backlog using the **Sprint Milestone**. Issues assigned to the `Sprint 1 – MVP v1` milestone represent the current Sprint Backlog.

- Link to Sprint Milestone: [Sprint 1 – MVP v1](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/1)

## Two repositories
Our main repository is [`the_blimp_swp`](https://github.com/Innopolis-Robotics-Society/the_blimp_swp).  
The external [`ardupilot-for-custom-blimp`](https://github.com/Innopolis-Robotics-Society/ardupilot-for-custom-blimp) repository is used as a modified version of ArduPilot with Blimp support. Our system runs SITL from this repository and communicates with it via MAVLink.

## MVP v1 Scope
MVP v1 includes the following Must Have stories:
- US-12: SITL heartbeat (#1)
- US-13: Mission upload (#14)
- US-14: Position feedback (#4)
- US-15: Telemetry streaming (#15)
- US-21: SITL startup script (#22)
- US-22: Smoke-check automation (#23)

## Total Story Points
- Sprint 1: 26

## Current Status
All Must Have issues are closed. SITL works with MAVLink, mission upload, and telemetry. Smoke-check is in progress.

## Next Steps
- Finish remaining tasks for MVP v1
- Record video demonstration(done in the video with customer review)
- Create SemVer release

## Week 3 Documents
- [Reflection](reflection.md)
- [Retrospective](retrospective.md)
- [LLM Report](llm-report.md)
- [Customer Review Summary](customer-review-summary.md)
- [Customer Review Transcript](customer-review-transcript.md)

## Images
 - [Product Backlog](images/product-backlog.png)
 - [Sprint Backlog](images/sprint-backlog.png)
 - [Sprint milestone](images/milestone.png)
 - [MVP version field](images/sprint-backlog.png) (tracked via Sprint Milestone)
 - [SemVer release](images/release.png)
 - [Delivered MVP v1](images/mvp-demo.png)
 - [Example reviewed PR](images/reviewed-pr.png)
