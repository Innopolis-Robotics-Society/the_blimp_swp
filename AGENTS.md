# AGENTS.md – AI Agent Guidance

This file provides guidance for AI coding agents working in this repository. For human contributors, please refer to [CONTRIBUTING.md](./CONTRIBUTING.md).

## Repository Structure

- `mavlink_backend/` – Python FastAPI backend and MAVLink communication
- `sitl/` – Docker setup for ArduPilot SITL
- `QGC/` – Docker setup for QGroundControl
- `docs/` – all maintained documentation
- `reports/` – weekly sprint reports

## Setup and Verification Commands

- **Start full stack:** `docker compose up -d`
- **Run backend tests:** `pytest mavlink_backend/tests/`
- **Run tests with coverage:** `pytest --cov=mavlink_backend mavlink_backend/tests/`
- **Check links:** `lychee .` (or via CI)
- **Lint Python code:** `flake8 mavlink_backend/` or `ruff check mavlink_backend/`

## Workflow and Review Expectations

1. Create a branch from `main` named `<issue-number>-short-description`.
2. Make changes and ensure all local tests pass.
3. Open a Pull Request linked to the relevant issue.
4. At least one human review is required. The agent cannot approve its own PR.
5. Ensure CI passes (tests, linters, link checks, coverage).
6. Update `CHANGELOG.md` under `[Unreleased]` for any user-visible changes.

## Safety and Security Cautions (CRITICAL)

As an AI agent, you must strictly adhere to the following safety and privacy rules:
- **NEVER commit `.env` files, API keys, tokens, passwords, or any real credentials.**
- **NEVER commit PII (Personally Identifiable Information), real names, or email addresses.** Use pseudonyms or roles (e.g., `customer`, `user@example.com`).
- **NEVER commit raw recordings, private recording links, or exact private timecodes.**
- Always verify that new files are added to `.gitignore` if they contain secrets or generated artifacts.
- Use placeholders like `{{access_token}}` in documentation and code examples instead of real credentials.

## Quality Requirements

- Tests must pass.
- Critical modules must maintain at least 30% automated line coverage.
- Quality requirement tests (QRTs) must pass.
- For detailed testing strategy, see [docs/testing.md](./docs/testing.md).
- For the team's completion standards, see [docs/definition-of-done.md](./docs/definition-of-done.md).

## Deeper Documentation

- [Development Process](./docs/development-process.md)
- [Architecture and ADRs](./docs/architecture/)
- [Customer Handover](./docs/customer-handover.md)
