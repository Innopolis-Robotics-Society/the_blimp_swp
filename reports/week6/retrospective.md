# Sprint 4 Retrospective — Week 6

**Sprint:** Sprint 4  
**Period:** 06 July 2026 — 12 July 2026  
**Facilitator:** Arina (Scrum Master)  
**Date of retrospective:** 12 July 2026, 19:20 — 20:00 (MSK)  
**Participants:** Daniyar, Arina, Iuliana, Svetlana (all present)  
**Format:** Online (Discord), Mad Sad Glad + Start/Stop/Continue

---

## 1. Retrospective Format

We used a combined format:

1. **Mad Sad Glad** — each team member shared one item per category
2. **Start / Stop / Continue** — actionable process changes
3. **Action items** — concrete tasks with owners and deadlines
4. **Follow-up check** — review of action items from Sprint 3 retrospective

---

## 2. Mad Sad Glad

### Mad (Frustrations)

| Team Member | Item |
|-------------|------|
| Daniyar | Customer unavailability blocked the most important validation event of the sprint. We prepared everything and had no one to show it to. |
| Arina | We spent too much time during the sprint figuring out what to do after the meeting was cancelled, instead of executing a pre-agreed plan. |
| Iuliana | The backend restructuring took longer than expected because we underestimated the effort to migrate existing scripts without breaking SITL integration. |
| Svetlana | QGC Docker image was initially too large (1.2 GB) and slow to pull. We had to iterate twice to get it down to an acceptable size. |

### Sad (Disappointments)

| Team Member | Item |
|-------------|------|
| Daniyar | We did not send the trial release to the customer asynchronously earlier in the week. We waited for the meeting, which meant the customer had zero time to try the system before the end of the sprint. |
| Arina | Our contingency planning for external blockers is still weak. This is the second sprint where an external dependency (customer, TA) disrupted our plans. |
| Iuliana | We did not have a clear definition of "documentation complete" before we started writing. This led to rework on customer-handover.md. |
| Svetlana | The demo video for Demo Day is still not recorded, and Week 7 will be very busy. We should have started earlier. |

### Glad (Positives)

| Team Member | Item |
|-------------|------|
| Daniyar | The trial release v0.4.0 is genuinely stable. Internal testing caught real issues before they could reach the customer. |
| Arina | Code review quality was the best we have had. Reviewers caught real issues, not just style nits. |
| Iuliana | The test suite we added gives us confidence to make changes in Sprint 5 without breaking existing functionality. |
| Svetlana | QGC in Docker works seamlessly. The customer will be able to run the full stack with one command. |
| All | Team communication was strong throughout the sprint. Daily stand-ups were focused, and we adapted quickly when the meeting was cancelled. |

---

## 3. Start / Stop / Continue

### Start (Things we should begin doing)

1. **Send trial releases and documentation to the customer asynchronously at the start of each sprint**, not wait for a synchronous meeting. This gives the customer time to explore and prepares us for a more productive discussion.

2. **Define a written contingency plan during sprint planning** for any customer-facing milestone. The plan must specify: trigger condition, immediate actions, escalation path, and rescheduling procedure.

3. **Automate link validation in CI** for release notes and documentation. We spent too much manual time verifying that every link in release notes and handover documents points to the right place.

4. **Start Demo Day preparation in Week 6**, not Week 7. The demo video, slides, and rehearsal require more time than we allocated.

### Stop (Things we should stop doing)

1. **Stop treating customer meetings as single points of failure.** Every customer-facing deliverable needs an asynchronous fallback path.

2. **Stop under-scoping documentation tasks.** Writing useful contributor and agent guidance is a design activity, not a reporting activity. It should be estimated accordingly.

3. **Stop waiting until the end of the sprint to validate with the customer.** Mid-sprint check-ins would have given us time to react to feedback.

4. **Stop manual link checking before releases.** This should be automated.

### Continue (Things that are working well)

1. **Continue assigning explicit reviewers to every PBI.** This has significantly improved code review quality and accountability.

2. **Continue the SemVer + CHANGELOG + protected-branch release workflow.** It is mature and reliable.

3. **Continue internal "fresh-eyes" documentation reviews before customer-facing milestones.** They catch real issues.

4. **Continue honest reporting of blockers.** We did not fabricate progress when the customer meeting fell through. This preserves the integrity of our transition evidence.

5. **Continue daily stand-ups with strict timeboxing.** They keep the team aligned without consuming too much time.

---

## 4. Action Items from This Retrospective

| Action | Owner | Deadline | Sprint | Status |
|--------|-------|----------|--------|--------|
| Draft contingency plan template for customer-facing milestones | Arina | 14 July 2026 | Sprint 5 | To Do |
| Add Lychee link validation to CI pipeline for release notes | Iuliana | 15 July 2026 | Sprint 5 | To Do |
| Send trial release v0.4.0 and documentation to customer via email | Daniyar | 13 July 2026 | Sprint 4 (carry-over) | In Progress |
| Schedule Week 7 customer meeting with three alternative time slots | Daniyar | 13 July 2026 | Sprint 4 (carry-over) | In Progress |
| Record Demo Day demo video (under 2 minutes) | Svetlana | 16 July 2026 | Sprint 5 | To Do |
| Start Demo Day slide deck | Arina | 14 July 2026 | Sprint 5 | To Do |
| Define explicit "documentation complete" checklist in CONTRIBUTING.md | Arina | 15 July 2026 | Sprint 5 | To Do |

---

## 5. Follow-Up on Sprint 3 Retrospective Actions

We reviewed the action items from the Sprint 3 retrospective (Week 5):

| Action from Sprint 3 | Owner | Outcome | Status |
|----------------------|-------|---------|--------|
| Add type hints to all Python modules | Iuliana | Completed during backend restructuring in Sprint 4 | Done |
| Improve PR template with reviewer assignment field | Arina | Completed; PR template now requires reviewer | Done |
| Create ADR for Docker Compose architecture | Svetlana | Completed; ADR-005 merged | Done |
| Set up weekly async customer update email | Daniyar | Not completed — this contributed to the Week 6 blocker | Repeated as new action |

**Assessment:** 3 out of 4 actions from Sprint 3 were completed. The one that was not completed (async customer updates) directly contributed to the Week 6 issue. This reinforces the need for better follow-through on retrospective actions.

---

## 6. Experiments for Sprint 5

Based on this retrospective, we will run the following process experiments in Sprint 5:

### Experiment 1: Asynchronous Customer Engagement
**Hypothesis:** Sending the trial release and documentation to the customer at the start of the sprint, with specific questions, will result in more productive synchronous meetings and partial feedback even if the meeting is rescheduled.  
**Measurement:** Customer response time, quality of feedback received, number of issues resolved without a meeting.  
**Owner:** Daniyar

### Experiment 2: Contingency Planning in Sprint Planning
**Hypothesis:** Explicitly documenting a contingency plan for every customer-facing milestone during sprint planning will reduce reaction time when blockers occur.  
**Measurement:** Time from blocker identification to execution of fallback plan.  
**Owner:** Arina

### Experiment 3: Automated Link Validation
**Hypothesis:** Adding Lychee-based link validation to CI will eliminate manual link checking before releases and catch broken links earlier.  
**Measurement:** Number of broken links found in release notes, manual time spent on link verification.  
**Owner:** Iuliana

---

## 7. Team Morale and Health

| Aspect | Rating (1-5) | Notes |
|--------|--------------|-------|
| Team cohesion | 5 | Strong communication, mutual support |
| Confidence in product | 4 | Product is stable, but customer validation is pending |
| Confidence in process | 3 | Good practices in place, but contingency planning needs work |
| Workload balance | 4 | Sprint 4 was well-paced; Sprint 7 will be intense |
| Motivation | 4 | Team is proud of the work, slightly frustrated by the customer blocker |

**Overall assessment:** The team is healthy and motivated. The main risk for Sprint 5 is time pressure, not team dynamics.

---

## 8. Summary

Sprint 4 was technically successful but exposed gaps in our handling of external dependencies. The retrospective produced concrete actions to address these gaps: asynchronous customer engagement, written contingency plans, and automated link validation. We also acknowledged that Demo Day preparation needs to start earlier than we planned.

The team's morale remains high, and we enter Sprint 5 with a clear plan and a stable product. The key challenge will be executing under time pressure while maintaining quality.

---

## Related Artifacts

- [Week 6 Report](./README.md)
- [Sprint Review Summary](./sprint-review-summary.md)
- [Sprint Review Notes](./sprint-review-notes.md)
- [Reflection](./reflection.md)
- [LLM Report](./llm-report.md)
- [Sprint 3 Retrospective](../week5/retrospective.md)
- [Sprint 4 Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/4)
