# Sprint 4 Review Notes — Week 6

**Sprint:** Sprint 4  
**Sprint Goal:** Deliver a stable trial release (v0.4.0) for customer testing, prepare comprehensive handover documentation, and establish transition-readiness evidence.  
**Review Date:** 12 July 2026, 18:00 — 19:15 (MSK)  
**Location:** Online (Discord)  
**Facilitator:** Arina (Scrum Master)  
**Note-taker:** Arina

---

## Participants

| Name | Role | Present |
|------|------|---------|
| Daniyar | Product Owner | Yes |
| Arina | Scrum Master | Yes |
| Iuliana | Developer | Yes |
| Svetlana | Developer | Yes |
| Eugene Shlomov | Customer | No (unavailable) |

**Note:** Customer was invited but could not attend due to scheduling conflict. Team proceeded with internal review and prepared materials for customer validation in Week 7.

---

## Agenda

1. Sprint Goal review and achievement assessment
2. Demo of completed work
3. Review of trial release v0.4.0
4. Documentation review status
5. Transition readiness discussion
6. Identification of follow-up work for Sprint 5
7. Retrospective preview (what went well, what to improve)

---

## Detailed Notes

### 1. Sprint Goal Review (18:00 — 18:10)

**Daniyar (PO):**
- Sprint 4 goal was to deliver a stable trial release and prepare handover documentation
- All technical work completed successfully
- Main blocker: customer was unavailable for meeting and trial validation
- Team needs to decide: proceed with Week 7 planning assuming customer will be available, or prepare contingency

**Arina (SM):**
- Sprint velocity: 26 out of 28 story points completed (93%)
- Only Story #51 (customer meeting) remains incomplete due to external blocker
- All other stories completed and reviewed

**Team consensus:** Sprint goal partially achieved — technical deliverables complete, customer validation deferred.

---

### 2. Demo of Completed Work (18:10 — 18:35)

#### 2.1 QGroundControl Docker Integration (Svetlana)

**Svetlana:**
- Created `QGC/` directory with Dockerfile and configuration
- QGC now runs as a service in docker-compose.yml
- Tested connectivity: QGC container successfully connects to SITL via UDP
- Demo: showed QGC interface with vehicle telemetry appearing in real-time

**Iuliana (reviewer):**
- Code review completed, approved with minor suggestions (all addressed)
- Docker image size optimized (reduced from 1.2GB to 850MB)
- Startup time improved with health checks

**Daniyar:**
- This is a key deliverable for customer — simplifies setup significantly
- Customer no longer needs to install QGC locally

**Decision:** Feature complete, ready for customer demo.

#### 2.2 MAVLink Backend Restructuring (Iuliana)

**Iuliana:**
- Converted flat script structure into proper Python package with modules
- Implemented FastAPI-based REST API with automatic Swagger UI documentation
- Added connection pooling and retry logic for MAVLink communication
- Improved error messages and logging

**Demo:**
- Showed Swagger UI at http://localhost:8000/docs
- Demonstrated API endpoints: vehicle status, command sending, mission upload
- Showed error handling: what happens when SITL is not running

**Svetlana (reviewer):**
- Code review completed, approved
- Suggested adding type hints throughout (implemented)
- Suggested adding request validation (implemented)

**Daniyar:**
- This is a major improvement over previous version
- API is now properly documented and maintainable
- Test coverage is critical — need to verify it is comprehensive

**Decision:** Feature complete, well-reviewed, ready for production use.

#### 2.3 MAVLink Backend Test Suite (Iuliana)

**Iuliana:**
- Added 42 unit tests covering all backend modules
- Added 15 integration tests for API endpoints
- Configured pytest with coverage reporting
- Integrated into CI/CD pipeline — tests run on every PR
- Current coverage: 83%

**Demo:**
- Ran pytest with coverage report
- Showed CI/CD pipeline passing all checks
- Demonstrated what happens when a test fails (PR blocked)

**Arina:**
- This addresses the quality requirement from Assignment 5
- Tests are maintainable and well-documented

**Daniyar:**
- 83% coverage is good, but what about the remaining 17%?

**Iuliana:**
- Remaining 17% is mostly error handling paths and edge cases
- Could add more tests in Sprint 5 if time permits, but not critical for trial release

**Decision:** Test suite complete and integrated. Coverage acceptable for trial release.

---

### 3. Trial Release v0.4.0 Review (18:35 — 18:50)

**Daniyar:**
- Release v0.4.0 created on protected main branch
- SemVer tag applied correctly
- CHANGELOG.md updated with all user-visible changes
- All links verified and working

**Arina:**
- Release notes include:
  - Summary of changes
  - Link to Sprint 4 milestone
  - Link to run instructions
  - Link to customer-handover.md
  - Link to Week 6 report

**Svetlana:**
- Tested clean installation from release tag
- All services start correctly
- Documentation is accurate

**Iuliana:**
- Verified API endpoints work as documented
- QGC connects successfully
- No critical bugs found

**Daniyar:**
- Release is ready for customer trial
- Need to prepare access instructions for customer

**Decision:** Release v0.4.0 approved and ready for customer validation.

---

### 4. Documentation Review Status (18:50 — 19:00)

**Arina:**
- All customer-facing documents prepared:
  - README.md: updated with quick-start instructions
  - docs/customer-handover.md: comprehensive handover guide
  - CONTRIBUTING.md: detailed contributor guidelines
  - AGENTS.md: AI-assisted development guidelines
  - docs/user-acceptance-tests.md: UAT scenarios maintained

**Daniyar:**
- Customer was supposed to review these in Week 6 meeting
- Since meeting didn't happen, review is postponed to Week 7

**Iuliana:**
- Team validated documentation internally
- All setup instructions tested and verified
- Links between documents are valid

**Svetlana:**
- Hosted documentation site updated
- Search functionality working
- All pages render correctly

**Daniyar:**
- Documentation is complete and ready for customer review
- Need to schedule Week 7 meeting ASAP

**Decision:** Documentation complete, customer review pending.

---

### 5. Transition Readiness Discussion (19:00 — 19:05)

**Daniyar:**
- Current handover level: Ready for independent use
- Customer has not yet used the trial release
- Customer has not deployed on their side

**Arina:**
- What blocks customer from using it now?

**Daniyar:**
- Customer was unavailable for meeting
- Need to provide access instructions and gather feedback
- Once customer validates, we can confirm transition

**Iuliana:**
- From technical perspective, system is ready
- All components working, documentation complete
- Customer just needs to run docker compose up

**Svetlana:**
- Should we send customer the access instructions now via email?

**Daniyar:**
- Yes, send instructions and schedule Week 7 meeting
- Ask customer to try the system before meeting

**Decision:** Send access instructions to customer immediately, schedule Week 7 meeting.

---

### 6. Follow-Up Work for Sprint 5 (19:05 — 19:10)

**Daniyar:**
- Sprint 5 will focus on:
  1. Customer meeting and feedback collection
  2. UAT execution with customer
  3. Addressing customer-reported issues
  4. Finalizing transition documentation
  5. Delivering MVP v3 (v0.5.0)
  6. Demo Day preparation

**Arina:**
- Need to create Sprint 5 backlog with these items
- Story points estimation needed

**Iuliana:**
- What if customer reports major bugs?

**Daniyar:**
- Sprint 5 has buffer for fixes
- If critical issues found, may need to adjust scope
- Demo Day preparation is mandatory, cannot skip

**Svetlana:**
- Should we start Demo Day slides now?

**Daniyar:**
- Yes, start early — slides and demo video take time
- Assign someone to lead Demo Day preparation

**Arina:**
- I will coordinate Demo Day preparation
- Will create task in Sprint 5 backlog

**Decision:** Sprint 5 backlog created, Demo Day preparation assigned to Arina.

---

### 7. Retrospective Preview (19:10 — 19:15)

**Arina:**
- Quick preview for retrospective:
  - What went well?
  - What could be improved?

**Svetlana:**
- Went well: QGC integration, backend restructuring
- Could improve: earlier customer confirmation

**Iuliana:**
- Went well: test suite, code quality
- Could improve: more frequent customer check-ins

**Daniyar:**
- Went well: documentation, release process
- Could improve: contingency planning for customer unavailability

**Arina:**
- Will document these in retrospective.md

**Decision:** Retrospective items identified, will be documented separately.

---

## Action Items

| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Send access instructions to customer | Daniyar | 13 July 2026 | Pending |
| Schedule Week 7 customer meeting | Daniyar | 13 July 2026 | Pending |
| Create Sprint 5 backlog | Arina | 13 July 2026 | Pending |
| Start Demo Day slides | Arina | 14 July 2026 | Pending |
| Record demo video for Demo Day | Svetlana | 16 July 2026 | Pending |
| Complete retrospective.md | Arina | 13 July 2026 | Pending |
| Complete reflection.md | Daniyar | 13 July 2026 | Pending |
| Complete llm-report.md | Iuliana | 13 July 2026 | Pending |

---

## Decisions Made

1. **Sprint 4 goal partially achieved** — technical deliverables complete, customer validation deferred to Week 7
2. **Release v0.4.0 approved** — ready for customer trial
3. **Documentation complete** — customer review pending
4. **Sprint 5 scope defined** — focus on customer feedback, fixes, and MVP v3 delivery
5. **Demo Day preparation started** — Arina coordinating, Svetlana recording demo video
6. **Customer contact initiated** — access instructions to be sent immediately

---

## Risks Identified

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Customer unavailable in Week 7 | Medium | High | Schedule multiple meeting slots, proceed with internal validation |
| Customer reports critical bugs | Low | High | Sprint 5 has buffer, team on standby for fixes |
| Demo Day preparation time pressure | Medium | Medium | Start early, assign dedicated owner |
| MVP v3 delivery delayed | Low | High | Prioritize critical fixes, defer nice-to-haves |

---

## Next Meeting

**Date:** Week 7 (to be scheduled with customer)  
**Purpose:** Customer trial feedback, UAT execution, transition confirmation  
**Preparation:** Customer to try trial release v0.4.0 before meeting

---

## Related Artifacts

- [Sprint Review Summary](./sprint-review-summary.md)
- [Week 6 Report](./README.md)
- [Retrospective](./retrospective.md)
- [Reflection](./reflection.md)
- [Sprint 4 Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/4)
- [Release v0.4.0](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.4.0)
