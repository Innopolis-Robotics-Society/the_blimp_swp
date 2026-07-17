# Week 6 Reflection — Sprint 4

**Sprint:** Sprint 4

**Period:** 06 July 2026 — 12 July 2026

**Authors:** Team 19 (Daniyar, Arina, Iuliana, Svetlana)

**Date written:** 12 July 2026

---

## Learning points

### Docker integration is a transition strategy, not just developer convenience
Integrating QGroundControl into Docker during Sprint 4 turned out to be one of the most important transition-enabling moves. Previously, the customer had to install QGC locally and configure UDP connections manually. By containerizing QGC, we reduced the customer's setup to a single `docker compose up` command. We learned that for handover scenarios, every external tool the customer must install manually is a potential blocker. Containerization is not just a developer convenience — it is a transition strategy.

### Backend restructuring paid off in multiple ways
The restructuring of `mavlink_backend/` from a collection of scripts into a proper Python package with FastAPI was more work than we initially estimated (8 story points), but it paid off in three ways:
1. The Swagger UI at `/docs` gives the customer a self-service way to explore the API without reading code.
2. The test suite we added during the same sprint caught two regressions during final integration testing that would have surfaced during customer trial.
3. The package structure makes future maintenance by the customer's team significantly easier.

We learned that investing in code structure and tests during a "stabilization" sprint is not overhead — it directly reduces the support burden after handover.

### Release automation needs link validation
Creating release v0.4.0 went smoothly because we had already established the SemVer + CHANGELOG + protected-branch workflow. What surprised us was how much time we still spent verifying that every link in the release notes pointed to the right place. We learned that release automation should include link validation, not just build and test.

### Customer-facing documentation is a different genre
Writing `docs/customer-handover.md` forced us to confront a reality we had been avoiding: our documentation had been written primarily for developers and TAs, not for the customer who will maintain the project after we leave. Sections that seemed obvious to us (like which environment variables matter and which do not) were either missing or buried in technical prose. We learned that "documentation complete" is not a meaningful state until it has been validated by someone outside the team.

### Process documentation is a design activity
We initially scoped `CONTRIBUTING.md` and `AGENTS.md` as 3 story points total, treating them as minor documentation tasks. In reality, writing useful agent guidance required us to articulate our development workflow, code style expectations, and safety constraints more precisely than we ever had before. We learned that process documentation is a design activity, not a reporting activity. It should be scoped accordingly.

### Internal validation catches real issues
Since the customer meeting did not happen, we ran an internal documentation review where team members tried to follow the setup instructions as if they were first-time users. This caught three real problems:
1. The README referenced a port that had been changed in `docker-compose.yml` but not updated in the docs.
2. The troubleshooting section did not mention the most common failure mode (Docker Desktop not running on macOS).
3. The handover document did not clearly state which configuration values were required vs optional.

We learned that internal "fresh-eyes" reviews are a poor substitute for customer review, but they are much better than no review at all.

---

## Validated assumptions

### Assumption: Docker-based deployment would simplify handover
**Validated.** The full Docker stack (SITL + backend + QGC) starts with a single command. The customer no longer needs to install ArduPilot, Python dependencies, or QGC separately. This assumption was confirmed during internal testing.

### Assumption: FastAPI + Swagger UI would be sufficient for API documentation
**Validated.** The Swagger UI at `/docs` provides interactive API exploration. During internal review, team members could use the API without reading source code. This assumption was confirmed.

### Assumption: 83% test coverage would be enough for trial release
**Validated.** The test suite caught two regressions during final integration. No critical bugs were found in the trial release. This assumption was confirmed.

### Assumption: Customer would be available for Week 6 meeting
**Rejected.** The customer was unavailable during the scheduled meeting time. This assumption was rejected. The team did not have a contingency plan for this scenario, which exposed a gap in our planning process.

### Assumption: Documentation could be validated in a single meeting
**Rejected.** We entered Week 6 thinking of transition as something that would happen in a single meeting. In reality, transition is a multi-week process that includes preparation, trial, feedback, fixes, confirmation, and follow-up. This assumption was rejected.

### Assumption: Documentation alone would be sufficient for transition
**Partially rejected.** Our documentation is now comprehensive, but documentation alone does not create transition. The customer also needs confidence that the system works as described, a clear path to get help, ownership of the repository, and a sense that the team will be available. We addressed some of these, but others require direct customer interaction.

---

## Friction and gaps

### Customer unavailability blocked the most important validation event
The customer's unavailability was not foreseeable in detail, but the possibility of unavailability was foreseeable in general. We did not have a plan for this scenario. When the meeting fell through, we spent several hours figuring out what to do next instead of executing a pre-agreed fallback. This is a significant gap in our contingency planning.

### Asynchronous communication was underused
We relied heavily on synchronous meetings for customer interaction and did not make sufficient use of asynchronous channels (email, GitHub Discussions, shared documents). If we had sent the trial release and documentation to the customer earlier in the week with specific questions, we might have received partial feedback even without a meeting.

### "Ready for independent use" is a claim, not a fact
We marked the handover level as "Ready for independent use," but we have to acknowledge that this is a team self-assessment, not a customer-validated state. Until the customer actually runs the system and confirms the documentation is sufficient, this is an aspiration, not a fact.

### Documentation review should have started earlier
We treated documentation review as a Week 6 activity. In hindsight, we should have started in Week 5 so that Week 6 would be purely for validation and feedback incorporation, not for first-draft writing.

### Demo Day preparation is under-scoped
The demo video, slides, and rehearsal require more time than we allocated. We should have started Demo Day preparation in Week 6, not Week 7.

### Link validation is manual
We spent manual time verifying that every link in release notes and handover documents points to the right place. This should be automated in CI.

### No written contingency plan for customer-facing milestones
Every customer-facing milestone needs a documented contingency: "If the customer is unavailable, we will do X, Y, Z." This should be part of sprint planning, not an afterthought.

---

## Planned response

### Week 7 actions
1. **Send trial release and documentation to customer asynchronously at the start of Week 7** (PBI #52). This gives the customer time to try the system before the meeting.
2. **Schedule Week 7 customer meeting with three alternative time slots** (PBI #53). This reduces the risk of another missed meeting.
3. **Define a written contingency plan template for customer-facing milestones** (PBI #54). This will be used in Sprint 5 planning.
4. **Add Lychee-based link validation to CI** (PBI #55). This will eliminate manual link checking before releases.
5. **Start Demo Day preparation immediately** (PBI #56). Arina will coordinate, Svetlana will record the demo video.

### Process improvements for Sprint 5
1. **Asynchronous customer engagement experiment.** We will send the trial release and documentation to the customer at the start of the sprint, with specific questions. We will measure customer response time and quality of feedback received.
2. **Contingency planning in sprint planning.** We will explicitly document a contingency plan for every customer-facing milestone during sprint planning. We will measure time from blocker identification to execution of fallback plan.
3. **Automated link validation.** We will add Lychee-based link validation to CI. We will measure the number of broken links found in release notes and manual time spent on link verification.

### Documentation improvements
1. **Define explicit "documentation complete" checklist** in CONTRIBUTING.md. This will prevent ambiguity about when documentation is ready for customer review.
2. **Start documentation review earlier** in future sprints — ideally one sprint before the customer-facing milestone.

### Links to affected artifacts
- Sprint 5 milestone: [Milestone 5](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/5)
- Affected PBIs: #52, #53, #54, #55, #56
- Related documentation: [docs/customer-handover.md](../../docs/customer-handover.md), [CONTRIBUTING.md](../../CONTRIBUTING.md)
- Related report: [Week 6 Report](./README.md)

---

## Related artifacts

- [Week 6 Report](./README.md)
- [Sprint Review Summary](./sprint-review-summary.md)
- [Sprint Review Notes](./sprint-review-notes.md)
- [Retrospective](./retrospective.md)
- [LLM Report](./llm-report.md)
- [Customer Handover](../../docs/customer-handover.md)
