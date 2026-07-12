# Week 6 Reflection — Sprint 4

**Sprint:** Sprint 4  
**Period:** 06 July 2026 — 12 July 2026  
**Authors:** Team 19 (Daniyar, Arina, Iuliana, Svetlana)  
**Date written:** 12 July 2026

---

## 1. Overview

Week 6 was the first week of Assignment 6 and marked the beginning of the transition phase. The team entered Sprint 4 with a clear goal: deliver a stable trial release (v0.4.0), prepare handover documentation, and establish transition-readiness evidence. Technically, the sprint was successful — all planned product and documentation work was completed. However, the customer was unavailable for the planned meeting, which exposed a gap in our contingency planning and forced us to reflect on how we handle external dependencies.

This reflection focuses on what we learned from the trial release, the documentation review preparation, the missed customer meeting, and the transition blockers we discovered.

---

## 2. What We Learned from the Trial Release

### 2.1 Docker Integration as a Transition Enabler

The decision to integrate QGroundControl into Docker during Sprint 4 turned out to be one of the most important transition-enabling moves we made. Previously, the customer had to install QGC locally and configure UDP connections manually — a non-trivial barrier for someone who is not a Docker expert but also not a complete beginner. By containerizing QGC, we reduced the customer's setup to a single `docker compose up` command.

**Concrete learning:** For handover scenarios, every external tool the customer must install manually is a potential blocker. Containerization is not just a developer convenience — it is a transition strategy.

### 2.2 Backend Restructuring Paid Off

The restructuring of `mavlink_backend/` from a collection of scripts into a proper Python package with FastAPI was more work than we initially estimated (8 story points), but it paid off in three ways:

1. The Swagger UI at `/docs` gives the customer a self-service way to explore the API without reading code.
2. The test suite we added during the same sprint caught two regressions during final integration testing that would have surfaced during customer trial.
3. The package structure makes future maintenance by the customer's team significantly easier — they can add new endpoints without touching the core connection logic.

**Concrete learning:** Investing in code structure and tests during a "stabilization" sprint is not overhead — it directly reduces the support burden after handover.

### 2.3 Release Process Maturity

Creating release v0.4.0 went smoothly because we had already established the SemVer + CHANGELOG + protected-branch workflow in earlier assignments. What surprised us was how much time we still spent verifying that every link in the release notes pointed to the right place. This suggests that our release checklist could be more automated.

**Concrete learning:** Release automation should include link validation, not just build and test.

---

## 3. What We Learned from Documentation Review Preparation

### 3.1 Customer-Facing Documentation Is a Different Genre

Writing `docs/customer-handover.md` forced us to confront a reality we had been avoiding: our documentation had been written primarily for developers and TAs, not for the customer who will maintain the project after we leave. Sections that seemed obvious to us (like which environment variables matter and which do not) were either missing or buried in technical prose.

**Concrete learning:** "Documentation complete" is not a meaningful state until it has been validated by someone outside the team. We should have done this earlier — ideally in Week 4 or 5.

### 3.2 CONTRIBUTING.md and AGENTS.md Were Underestimated

We initially scoped `CONTRIBUTING.md` and `AGENTS.md` as 3 story points total, treating them as minor documentation tasks. In reality, writing useful agent guidance required us to articulate our development workflow, code style expectations, and safety constraints more precisely than we ever had before. The resulting documents are now among the most useful artifacts in the repository — not just for the customer, but for us.

**Concrete learning:** Process documentation is a design activity, not a reporting activity. It should be scoped accordingly.

### 3.3 Internal Validation Caught Real Issues

Since the customer meeting did not happen, we ran an internal documentation review where team members tried to follow the setup instructions as if they were first-time users. This caught three real problems:

1. The README referenced a port that had been changed in `docker-compose.yml` but not updated in the docs.
2. The troubleshooting section did not mention the most common failure mode (Docker Desktop not running on macOS).
3. The handover document did not clearly state which configuration values were required vs optional.

**Concrete learning:** Internal "fresh-eyes" reviews are a poor substitute for customer review, but they are much better than no review at all. We should make this a standard practice before any customer-facing milestone.

---

## 4. What We Learned from the Missed Customer Meeting

### 4.1 External Dependencies Need Explicit Contingency

The customer's unavailability was not foreseeable in detail, but the possibility of unavailability was foreseeable in general. We did not have a plan for this scenario. When the meeting fell through, we spent several hours figuring out what to do next instead of executing a pre-agreed fallback.

**Concrete learning:** Every customer-facing milestone needs a documented contingency: "If the customer is unavailable, we will do X, Y, Z." This should be part of sprint planning, not an afterthought.

### 4.2 Asynchronous Communication Was Underused

We relied heavily on synchronous meetings for customer interaction and did not make sufficient use of asynchronous channels (email, GitHub Discussions, shared documents). If we had sent the trial release and documentation to the customer earlier in the week with specific questions, we might have received partial feedback even without a meeting.

**Concrete learning:** Synchronous meetings should be for discussion and decision-making, not for initial information transfer. Documentation and trial releases can be shared asynchronously well before the meeting.

### 4.3 The Blocker Was Honest and Documented

On the positive side, we did not pretend the meeting happened or fabricate feedback. The Week 6 report clearly states that the customer was unavailable, the impact is documented, and the mitigation (reschedule for Week 7) is explicit. This honesty is important for the integrity of the transition process.

**Concrete learning:** Reporting blockers accurately is more valuable than reporting progress optimistically.

---

## 5. What We Learned About Transition Readiness

### 5.1 "Ready for Independent Use" Is a Claim, Not a Fact

We marked the handover level as "Ready for independent use," but we have to acknowledge that this is a team self-assessment, not a customer-validated state. Until the customer actually runs the system and confirms the documentation is sufficient, this is an aspiration, not a fact.

**Concrete learning:** Handover levels should be treated as hypotheses to be validated, not statuses to be declared.

### 5.2 Transition Is a Process, Not an Event

We entered Week 6 thinking of transition as something that would happen in a single meeting. In reality, transition is a multi-week process that includes preparation, trial, feedback, fixes, confirmation, and follow-up. Sprint 4 was the preparation phase; Sprint 5 will be the trial and confirmation phase.

**Concrete learning:** Future assignments should introduce transition readiness earlier — not as a Week 6 activity, but as a continuous thread from Week 3 onward.

### 5.3 The Documentation Is Necessary but Not Sufficient

Our documentation is now comprehensive, but documentation alone does not create transition. The customer also needs:

- Confidence that the system works as described
- A clear path to get help when something goes wrong
- Ownership of the repository and deployment environment
- A sense that the team will be available during the transition period

We addressed some of these (help path via GitHub Issues, team availability stated in handover doc), but others (confidence, ownership) require direct customer interaction.

**Concrete learning:** Transition is as much about trust and ownership as it is about documentation.

---

## 6. Team Process Reflection

### 6.1 Sprint Planning Was Realistic

Our story point estimates for Sprint 4 were accurate. The only story that did not complete (#51, customer meeting) was blocked by an external factor, not by estimation error. This suggests our planning process has matured.

### 6.2 Code Review Quality Improved

Reviews during Sprint 4 were more thorough than in earlier sprints. Reviewers consistently caught real issues (type hints, request validation, Docker image size) rather than just rubber-stamping PRs. This is likely because we added explicit reviewer assignment in Assignment 5 and started tracking review quality.

### 6.3 Communication Within the Team Was Strong

Daily stand-ups were short and focused. When the customer meeting fell through, the team adapted quickly without drama. The Scrum Master facilitated effectively, and the Product Owner made clear priority decisions.

---

## 7. What We Would Do Differently

If we were starting Sprint 4 again, we would:

1. **Send the trial release and documentation to the customer asynchronously at the start of the week**, not wait for the meeting. This would have given the customer time to try the system and prepared us for a more productive meeting.

2. **Define a written contingency plan during sprint planning** for the case where the customer is unavailable. The plan would have specified: "If customer does not respond by Wednesday, we send a follow-up email, proceed with internal validation, and reschedule for next week."

3. **Start documentation review earlier** — ideally in Week 5 — so that Week 6 is purely for validation and feedback incorporation, not for first-draft writing.

4. **Automate release link validation** as part of the CI pipeline, so we do not spend manual time checking that every link in release notes works.

5. **Treat the customer meeting as a hard dependency** and schedule it earlier in the sprint, with buffer time for rescheduling. Waiting until the end of the sprint left us no room to recover.

---

## 8. Looking Ahead to Week 7

Week 7 is our final sprint before Demo Day. The priorities are clear:

1. Conduct the customer meeting and collect real feedback
2. Execute UAT with the customer
3. Address any issues found during trial
4. Deliver MVP v3 (final release v0.5.0)
5. Confirm transition with the customer
6. Prepare Demo Day presentation and demo video

The risk is time pressure — we have a lot to do in one week. The mitigation is strict prioritization: customer feedback and MVP v3 delivery are mandatory; everything else is secondary.

We enter Week 7 with a stable product, comprehensive documentation, and a clear plan. The main unknown is the customer's response to the trial release. Whatever that response is, we are prepared to adapt.

---

## 9. Summary

Week 6 was a sprint of technical success and process learning. We delivered everything we planned to deliver, but we also discovered that our transition process had gaps — particularly around contingency planning and asynchronous customer communication. These are not failures; they are the kind of learnings that only emerge when you actually try to hand over a real product to a real customer.

The team is stronger going into Week 7 than we were at the start of Week 6. We have a better understanding of what transition actually means, and we have concrete improvements to make in our process. The product is ready; now we need to validate it with the customer and close the loop.

---

## Related Artifacts

- [Week 6 Report](./README.md)
- [Sprint Review Summary](./sprint-review-summary.md)
- [Sprint Review Notes](./sprint-review-notes.md)
- [Retrospective](./retrospective.md)
- [LLM Report](./llm-report.md)
- [Customer Handover](../../docs/customer-handover.md)
