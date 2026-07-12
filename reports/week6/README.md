# Week 6 Report — Sprint 4

## Project Information

**Project name:** Autonomous Indoor Airship Simulation
**Team number:** 19
**Customer:** Eugene Shlomov (Innopolis Robotics Lab)
**License:** [MIT License](../../LICENSE)
**Assignment:** Assignment 6 — Sprint 4 (Trial Release & Transition Readiness)

---

## Links

### Backlogs and Milestones
- [Product Backlog](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues)
- [Sprint 4 Backlog (GitHub Projects)](https://github.com/orgs/Innopolis-Robotics-Society/projects/4/views/1)
- [Sprint 4 Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/4)
- [Sprint 5 Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/5)

### Documentation
- [README.md](../../README.md)
- [CONTRIBUTING.md](../../CONTRIBUTING.md)
- [AGENTS.md](../../AGENTS.md)
- [Customer Handover](../../docs/customer-handover.md)
- [Hosted Documentation](https://innopolis-robotics-society.github.io/the_blimp_swp/)
- [Roadmap](../../docs/roadmap.md)
- [CHANGELOG.md](../../CHANGELOG.md)
- [Architecture and ADRs](../../docs/architecture/)
- [User Acceptance Tests](../../docs/user-acceptance-tests.md)
- [User Stories](../../docs/user-stories.md)

### Releases and Reports
- [Week 6 Trial Release v0.4.0](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.4.0)
- [Week 5 Report](../week5/README.md)

---

## Sprint 4 Overview

### Sprint 4 Goal
Deliver a stable trial release (v0.4.0) for customer testing, prepare comprehensive handover documentation, and establish transition-readiness evidence.

### Sprint Dates
- **Start:** 06 July 2026
- **Finish:** 12 July 2026

### Sprint 4 Scope (Selected PBIs)

| Story ID | Title | Story Points | Implementer | Reviewer | Status |
|----------|-------|--------------|-------------|----------|--------|
| #45 | Integrate QGroundControl in Docker | 5 | Svetlana | Iuliana | Done |
| #46 | Restructure mavlink_backend as Python package | 8 | Iuliana | Svetlana | Done |
| #47 | Add comprehensive test suite for MAVLink backend | 5 | Iuliana | Daniyar | Done |
| #48 | Update customer-handover.md with current state | 3 | Arina | Daniyar | Done |
| #49 | Prepare CONTRIBUTING.md and AGENTS.md | 3 | Arina | Svetlana | Done |
| #50 | Create trial release v0.4.0 | 2 | Daniyar | Arina | Done |
| #51 | Schedule and document customer meeting | 2 | Daniyar | Arina | Blocked (customer unavailable) |

**Total Sprint 4 Story Points:** 28

---

## Summary of Week 6 Trial-Release Changes

### What is New in v0.4.0

1. **QGroundControl Docker Integration**
   - Added `QGC/` directory with Docker configuration
   - QGC now runs in container alongside SITL and backend
   - Simplified visualization setup for customers

2. **MAVLink Backend Restructuring**
   - Converted `mavlink_backend/` from flat scripts to proper Python package
   - Implemented FastAPI-based REST API with Swagger UI
   - Added comprehensive test suite (unit + integration tests)
   - Improved error handling and connection management

3. **Documentation Updates**
   - Updated `docs/customer-handover.md` with current deployment state
   - Enhanced `CONTRIBUTING.md` with detailed PR workflow
   - Added `AGENTS.md` for AI-assisted development guidelines
   - Updated root `README.md` with quick-start instructions

4. **Infrastructure Improvements**
   - Enhanced `docker-compose.yml` with better service orchestration
   - Improved SITL Docker configuration for stability
   - Added CI/CD workflows for automated testing

### Deployment URL / Access Artifact

**Trial Release Access:**
- **Release:** [v0.4.0](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.4.0)
- **Run Instructions:** See [Quick Start](../../README.md#quick-start) in root README
- **API Documentation:** http://localhost:8000/docs (after `docker compose up`)
- **QGroundControl:** Connects automatically via Docker network

---

## Customer-Facing Documentation Review

### Documents Reviewed
- [x] `README.md`
- [x] `docs/customer-handover.md`
- [x] Current access/usage instructions
- [x] Deployment/installation instructions
- [x] Troubleshooting notes
- [x] Known limitations

### Review Status
**Customer meeting did not occur in Week 6** — customer was unavailable.

The team prepared all documentation for review and scheduled a meeting for Week 7. Documentation is complete and ready for customer validation.

**What the team validated internally:**
- All setup instructions are accurate and reproducible
- Docker Compose starts all services correctly
- API endpoints are documented and functional
- Links between documents are valid
- Known limitations are clearly stated

### Customer Feedback Response Table

| Feedback Point | Resulting PBI/Issue | Status | Notes |
|----------------|---------------------|--------|-------|
| (No feedback yet) | — | — | Customer meeting pending for Week 7 |

**Explanation:** Customer was unavailable during Week 6. All feedback will be collected and addressed in Sprint 5 (Week 7).

---

## Transition-Readiness Summary

### Current Handover Level
- [x] **Ready for independent use**
- [ ] Independently used by customer
- [ ] Deployed or operated on customer side

### What Must Happen in Week 7
1. Conduct customer meeting to gather feedback
2. Address any issues identified during customer trial
3. Obtain customer confirmation on handover documentation
4. Complete final transition to customer
5. Deliver MVP v3 release

### Transition Evidence
- Trial release v0.4.0 deployed and accessible
- Comprehensive documentation prepared
- All setup instructions verified internally
- Customer validation pending (Week 7)

---

## User Acceptance Tests (UAT)

### UAT Scenarios Maintained
See [docs/user-acceptance-tests.md](../../docs/user-acceptance-tests.md) for full test suite.

### UAT Execution Status
**UAT not executed with customer in Week 6** — customer unavailable.

**Internal UAT Results (team-executed):**

| Test ID | Scenario | Result | Notes |
|---------|----------|--------|-------|
| UAT-01 | Start all services with Docker Compose | Pass | All containers start successfully |
| UAT-02 | Access API documentation | Pass | Swagger UI loads at /docs |
| UAT-03 | Connect QGroundControl to vehicle | Pass | Vehicle appears in QGC |
| UAT-04 | Send MAVLink command via API | Pass | Command executed successfully |
| UAT-05 | Upload mission plan | Pass | Mission uploaded and verified |

**Failed/Incomplete Tests:** None

---

## Contribution Traceability Table

| Team Member | Role | Issues Worked | PRs/MRs | Reviews | Testing | Documentation | Deployment |
|-------------|------|---------------|---------|---------|---------|---------------|------------|
| Daniyar | Product Owner | #50, #51 | Release v0.4.0 | All PRs | UAT coordination | README, handover docs | Release management |
| Arina | Scrum Master | #48, #49 | CONTRIBUTING.md, AGENTS.md | #45, #46 | Process validation | Sprint docs, reflection | — |
| Iuliana | Developer | #46, #47 | mavlink_backend restructuring | #45 | Test suite | API docs | Backend Docker config |
| Svetlana | Developer | #45 | QGC Docker setup | #46, #47 | Integration tests | QGC docs | Docker compose |

---

## Sprint Review Artifacts

### Sprint Review Summary
See [sprint-review-summary.md](./sprint-review-summary.md)

### Sprint Review Notes
See [sprint-review-notes.md](./sprint-review-notes.md)

**Note:** Recording and private sharing were refused. Detailed notes are provided instead.

---

## Reflection and Retrospective

### Week 6 Reflection
See [reflection.md](./reflection.md)

### Week 6 Retrospective
See [retrospective.md](./retrospective.md)

---

## LLM Usage Report

See [llm-report.md](./llm-report.md)

---

## Current Product Status

### What Works
- Full Docker-based deployment (SITL + MAVLink backend + QGC)
- Comprehensive test suite with CI/CD
- Complete documentation suite
- Trial release v0.4.0 is stable and accessible

### What Is Pending
- Customer validation of trial release
- Final feedback incorporation
- MVP v3 final delivery
- Demo Day preparation

---

## Expected Week 7 Follow-Up Work

1. **Customer Meeting and Feedback Collection**
   - Conduct transition-readiness meeting
   - Gather customer feedback on trial release
   - Document all feedback as PBIs

2. **Final Fixes and Improvements**
   - Address customer-reported issues
   - Polish documentation based on feedback
   - Final testing and validation

3. **MVP v3 Delivery**
   - Create final release v0.5.0 (MVP v3)
   - Update all documentation
   - Complete transition to customer

4. **Demo Day Preparation**
   - Prepare presentation slides
   - Record demo video
   - Rehearse presentation

---

## Screenshots and Evidence

### Sprint 4 Milestone
![Sprint 4 Milestone](./images/sprint4-milestone.png)

### Week 6 Release v0.4.0
![Release v0.4.0](./images/release-v0.4.0.png)

### Example Reviewed PR
![Reviewed PR Example](./images/reviewed-pr-example.png)

### QGroundControl Running in Docker
![QGC in Docker](./images/qgc-docker.png)

### API Documentation (Swagger UI)
![API Docs](./images/api-docs.png)
