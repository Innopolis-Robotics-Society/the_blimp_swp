# AGENTS.md – AI Agent Guidance

This file provides guidance for AI agents working on this repository.

## Repository structure

- `mavlink_backend/` – backend API and MAVLink communication
- `sitl/` – Docker setup for ArduPilot SITL
- `docs/` – all documentation
- `reports/` – weekly reports

## Key files

- `README.md` – main entry point
- `CONTRIBUTING.md` – how to contribute
- `docs/customer-handover.md` – handover guide for the customer
- `docs/definition-of-done.md` – what "done" means

## Workflow

1. Create a branch from `main`.
2. Make changes.
3. Open a Pull Request.
4. At least one review is required.
5. CI must pass (tests, linters, link checks).

## Documentation updates

- Update `CHANGELOG.md` for user-visible changes.
- Update `README.md` if setup or usage changes.
- Update `docs/customer-handover.md` when handover status changes.

## Quality requirements

- Tests must pass.
- Coverage must be at least 30% for critical modules.
- Quality requirement tests (QRTs) must pass.

## Questions?

Refer to the team or open an issue.
