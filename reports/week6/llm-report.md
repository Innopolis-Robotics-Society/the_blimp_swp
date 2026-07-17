# LLM Usage Report — Week 6 (Sprint 4)

**Sprint:** Sprint 4  
**Period:** 06 July 2026 — 12 July 2026  
**Authors:** Team 19 (Daniyar, Arina, Iuliana, Svetlana)  
**Date written:** 12 July 2026

---

## 1. Summary

During Sprint 4, the team used LLM tools minimally and only for specific routine tasks. All LLM-assisted content was reviewed, verified, and edited by team members before being committed. No AI-generated content was accepted without human review. No code was committed based solely on LLM suggestions.

---

## 2. Tools Used

| Tool | Used By | Purpose |
|------|---------|---------|
| GitHub Copilot | Iuliana, Svetlana | Inline code completion for type hints and boilerplate |
| ChatGPT (GPT-4) | Arina | Brief brainstorming of handover document structure |

---

## 3. Usage Details

### 3.1 Code Completion (GitHub Copilot)

Iuliana and Svetlana used Copilot inline suggestions during:
- Adding type hints to Python functions in `mavlink_backend/`
- Writing boilerplate for FastAPI route handlers
- Drafting initial Dockerfile for QGroundControl

Approximately 50-60% of suggestions were accepted after verification. The rest were rejected or rewritten because they did not match the project's patterns or contained incorrect logic. All accepted code was reviewed by the assigned reviewer and tested in CI before merge.

### 3.2 Documentation Brainstorming (ChatGPT)

Arina used ChatGPT briefly to generate a list of typical handover document sections. The output was used only as a checklist to ensure no obvious sections were missed. All actual content was written by the team based on the real state of the project.

---

## 4. What Was NOT Used For

The team explicitly did NOT use LLM tools for:
- Writing Sprint Review notes, reflection, or retrospective content
- Generating customer feedback or meeting outcomes
- Writing code without review and testing
- Drafting the Week 6 report

---

## 5. Risks and Mitigations

The main risk encountered was that Copilot suggestions sometimes contained incorrect logic (especially for connection handling). This was mitigated by:
- Mandatory code review by the assigned reviewer
- Running the full test suite before merge
- Rejecting suggestions that did not match existing patterns

No LLM-introduced bugs reached the repository.

---

## 6. Value Assessment

LLM tools provided modest assistance with routine tasks (type hints, boilerplate). The net time saving was small, and the value was highest for repetitive work. For creative or project-specific tasks, the team found that writing from scratch was faster than reviewing LLM output.

---

## 7. Policy

The team will continue the following policies:
1. All LLM-assisted content must be reviewed by a human before commit.
2. No LLM-generated code may be committed without testing and code review.
3. LLM tools may not be used to fabricate evidence or meeting outcomes.
4. LLM usage must be reported transparently in weekly reports.

---

## 8. Declaration

The team declares that all content committed during Sprint 4 was reviewed and approved by team members. No LLM-generated content was committed without human review. The team retains full responsibility for all committed content.

---

## Related Artifacts

- [Week 6 Report](./README.md)
- [Sprint Review Summary](./sprint-review-summary.md)
- [Reflection](./reflection.md)
- [Retrospective](./retrospective.md)
- [CONTRIBUTING.md](../../CONTRIBUTING.md)
- [AGENTS.md](../../AGENTS.md)
