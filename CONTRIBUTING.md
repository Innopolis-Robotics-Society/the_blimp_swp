# Contributing to the_blimp_swp

Thank you for your interest in contributing to our project! This document outlines the workflow and expectations for human contributors. For AI coding agents, please refer to [AGENTS.md](./AGENTS.md).

## Development Workflow

1. **Find an issue:** Check the [Issues](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/issues) page.
2. **Create a branch:** Create a branch from `main` using the format `<issue-number>-short-description` (e.g., `42-add-mavlink-command`).
3. **Make changes:** Follow our coding style (Python: PEP 8, clear variable names, docstrings).
4. **Verify locally:** Run tests and linters locally before pushing.
5. **Open a Pull Request:** Link the PR to the issue. Ensure the PR description includes a summary of changes and testing performed.
6. **Wait for review:** At least one team member must approve the PR. The author cannot approve their own PR.
7. **Merge:** Once approved and CI passes, the PR is merged using a merge commit (no squash/rebase).

## Review Expectations and Definition of Done

A contribution is only considered "Done" when it satisfies the team's [Definition of Done](./docs/definition-of-done.md). At a minimum, this means:
- All issue acceptance criteria are satisfied.
- The work is reviewed by another team member.
- Required tests pass and CI quality gates are green.
- `CHANGELOG.md` is updated for any user-visible changes.
- Relevant documentation (e.g., `README.md`, `docs/customer-handover.md`) is updated if setup or usage changed.

## Testing and CI

- Run `pytest mavlink_backend/tests/` to run all backend tests.
- Add unit or integration tests for new features.
- Our CI pipeline automatically runs linting, type checking, unit/integration tests, coverage reporting, and link checking (Lychee) on every PR. Your PR must pass all CI checks before it can be merged.
- For detailed testing strategy and coverage expectations, see [docs/testing.md](./docs/testing.md).

## Documentation

- Update `README.md` if you change setup or usage instructions.
- Update `CHANGELOG.md` with your changes under the `[Unreleased]` section.
- Update `docs/customer-handover.md` if deployment steps, environment variables, or known limitations change.

## Deeper Documentation

For more details on our processes and architecture, please refer to:
- [Development Process](./docs/development-process.md)
- [Definition of Done](./docs/definition-of-done.md)
- [Architecture and ADRs](./docs/architecture/)
- [Quality Requirements](./docs/quality-requirements.md)

## Questions?

Ask in the team chat, open a GitHub Discussion, or comment on the relevant issue.
