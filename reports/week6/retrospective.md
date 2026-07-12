# Sprint 4 Retrospective — Week 6

**Sprint:** Sprint 4
**Period:** 06 July 2026 — 12 July 2026
**Facilitator:** Arina (Scrum Master)
**Date of retrospective:** 12 July 2026
**Participants:** Daniyar, Arina, Iuliana, Svetlana (all present)

---

## What went well

### QGroundControl Docker integration works seamlessly
Svetlana successfully integrated QGC into Docker, reducing the customer's setup to a single `docker compose up` command. The Docker image was optimized from 1.2 GB to 850 MB through iteration. The integration was reviewed by Iuliana and tested thoroughly. This is a key deliverable for the customer and significantly simplifies the handover.

### MAVLink backend restructuring improved code quality significantly
Iuliana converted `mavlink_backend/` from flat scripts into a proper Python package with FastAPI. The Swagger UI at `/docs` provides self-service API exploration. The test suite (42 unit tests + 15 integration tests, 83% coverage) caught two regressions during final integration. The restructuring was reviewed by Svetlana and makes future maintenance much easier.

### Code review quality was the best we have had
Reviewers consistently caught real issues (type hints, request validation, Docker image size) rather than just rubber-stamping PRs. This is likely because we added explicit reviewer assignment in Assignment 5 and started tracking review quality. All PRs in Sprint 4 had meaningful reviews with substantive comments.

### Team communication was strong throughout the sprint
Daily stand-ups were short and focused. When the customer meeting fell through, the team adapted quickly without drama. The Scrum Master facilitated effectively, and the Product Owner made clear priority decisions. Team morale remained high despite the customer unavailability blocker.

### Documentation is comprehensive and well-structured
Arina updated `docs/customer-handover.md` with current deployment state, environment variables, troubleshooting steps, and verification procedures. `CONTRIBUTING.md` and `AGENTS.md` were created with detailed workflow guidance. The documentation was validated internally and caught three real problems (incorrect port reference, missing troubleshooting case, unclear required vs optional configuration).

---

## What did not go well

### Customer unavailability blocked the most important validation event
The customer was unavailable during the scheduled meeting time. We prepared everything and had no one to show it to. This is the second sprint where an external dependency (customer, TA) disrupted our plans. We did not have a contingency plan for this scenario, which meant we spent several hours figuring out what to do next instead of executing a pre-agreed fallback.

### We did not send the trial release to the customer asynchronously earlier
We waited for the meeting to share the trial release, which meant the customer had zero time to try the system before the end of the sprint. If we had sent the release and documentation via email at the start of the week, we might have received partial feedback even without a meeting.

### Contingency planning for external blockers is still weak
This is the second sprint where an external dependency disrupted our plans. We need a written contingency plan for every customer-facing milestone: "If the customer is unavailable, we will do X, Y, Z." This should be part of sprint planning, not an afterthought.

### Demo Day preparation is under-scoped and starting too late
The demo video, slides, and rehearsal require more time than we allocated. We should have started Demo Day preparation in Week 6, not Week 7. Week 7 will be very busy with customer feedback, fixes, and MVP v3 delivery.

### Documentation tasks were under-scoped
We initially scoped `CONTRIBUTING.md` and `AGENTS.md` as 3 story points total, treating them as minor documentation tasks. In reality, writing useful agent guidance required us to articulate our development workflow, code style expectations, and safety constraints more precisely than we ever had before. The actual effort was closer to 5 story points.

### Link validation before releases is manual and time-consuming
We spent manual time verifying that every link in release notes and handover documents points to the right place. This should be automated in CI. The manual process is error-prone and consumes time that could be spent on higher-value work.

---

## What the team changed or attempted to change based on the previous Sprint Retrospective, and what results they observed

### Previous retrospective action: Add type hints to all Python modules (Owner: Iuliana)
**Result:** Completed during backend restructuring in Sprint 4. All Python modules in `mavlink_backend/` now have comprehensive type hints. This improved code readability and caught several type-related bugs during development. **Status: Done.**

### Previous retrospective action: Improve PR template with reviewer assignment field (Owner: Arina)
**Result:** Completed. PR template now requires explicit reviewer assignment. All PRs in Sprint 4 had assigned reviewers, and review quality improved significantly. **Status: Done.**

### Previous retrospective action: Create ADR for Docker Compose architecture (Owner: Svetlana)
**Result:** Completed. ADR-005 documenting the Docker Compose architecture decision was merged. This ADR is now referenced from `docs/architecture/README.md` and helps new team members understand the deployment model. **Status: Done.**

### Previous retrospective action: Set up weekly async customer update email (Owner: Daniyar)
**Result:** Not completed. This directly contributed to the Week 6 blocker — we did not have an established async communication channel with the customer, so when the meeting fell through, we had no fallback. **Status: Repeated as new action for Sprint 5.**

**Assessment:** 3 out of 4 actions from Sprint 3 retrospective were completed. The one that was not completed (async customer updates) directly contributed to the Week 6 issue. This reinforces the need for better follow-through on retrospective actions.

---

## Action points

### Action 1: Send trial release and documentation to customer asynchronously at the start of Sprint 5
**Owner:** Daniyar
**Deadline:** 13 July 2026 (start of Sprint 5)
**Description:** Send the trial release v0.4.0, `docs/customer-handover.md`, and specific questions to the customer via email. This gives the customer time to explore the system before the synchronous meeting and provides a fallback if the meeting is rescheduled.
**Success criteria:** Customer receives the email and acknowledges receipt. Customer has at least 3 days to try the system before the Week 7 meeting.

### Action 2: Define a written contingency plan template for customer-facing milestones
**Owner:** Arina
**Deadline:** 14 July 2026
**Description:** Create a template that specifies: trigger condition (e.g., "customer does not respond by Wednesday"), immediate actions (e.g., "send follow-up email"), escalation path (e.g., "contact TA"), and rescheduling procedure. Use this template during Sprint 5 planning for the Week 7 customer meeting.
**Success criteria:** Template is documented in `docs/development-process.md` and used in Sprint 5 planning.

### Action 3: Add Lychee-based link validation to CI for release notes
**Owner:** Iuliana
**Deadline:** 15 July 2026
**Description:** Configure Lychee to validate all links in release notes and handover documents as part of the CI pipeline. This will eliminate manual link checking before releases and catch broken links earlier.
**Success criteria:** Lychee job runs on every PR and protected-branch push. Broken links cause CI failure.

### Action 4: Start Demo Day preparation immediately
**Owner:** Arina (coordination), Svetlana (demo video)
**Deadline:** 14 July 2026 (slides), 16 July 2026 (demo video)
**Description:** Start Demo Day slide deck and record the demo video (under 2 minutes) early in Week 7. This reduces time pressure later in the sprint.
**Success criteria:** Slide deck draft completed by 14 July. Demo video recorded and reviewed by 16 July.

---

## Related artifacts

- [Week 6 Report](./README.md)
- [Sprint Review Summary](./sprint-review-summary.md)
- [Sprint Review Notes](./sprint-review-notes.md)
- [Reflection](./reflection.md)
- [LLM Report](./llm-report.md)
- [Sprint 3 Retrospective](../week5/retrospective.md)
- [Sprint 4 Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/4)
