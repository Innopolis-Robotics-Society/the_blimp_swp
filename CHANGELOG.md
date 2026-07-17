# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

No planned changes.

## [v0.5.0] - 2026-07-17 - Final MVP (Sprint 5)

Final release of the Autonomous Indoor Airship Simulation project.

This release concludes the Software Engineering course project and includes the completed implementation, final documentation, customer handover, and project acceptance.

### Added

- Sprint 5 documentation (`reports/week7/`)
- Final Sprint Review summary and transcript
- Sprint Reflection
- Sprint Retrospective
- LLM Usage Report
- Final customer handover documentation
- Final project release (MVP v3)

### Changed

- Updated repository documentation following customer review
- Updated root README for the final project release
- Updated roadmap to reflect project completion
- Finalized project documentation for long-term maintenance

### Fixed

- Minor documentation inconsistencies identified during the final repository review
- Cross-references between documentation artifacts

### Security

- Verified that no credentials, secrets, or sensitive information are stored in the repository

### Documentation

- Release v0.5.0
- Week 7 Report (`reports/week7/README.md`)
- Customer Handover (`docs/customer-handover.md`)
- Sprint Review documentation (`reports/week7/`)

The Software Engineering project has been completed, and the repository reflects the final accepted state of the project.
## [v0.4.0] - 2026-07-10 - Week 6 Trial Release (Sprint 4)

Trial release for customer testing and handover preparation. This release is the Assignment 6 Week 6 deliverable and represents the handover-candidate version of the product.

### Added
- QGroundControl Docker integration (`QGC/` directory) - QGC now runs as a container alongside SITL and the backend, removing the need for a local QGC installation
- FastAPI-based REST API for MAVLink communication with Swagger UI at `/docs`
- Comprehensive test suite for `mavlink_backend/` (unit + integration tests, ~83% coverage)
- `AGENTS.md` with AI-assisted development guidelines
- Enhanced `CONTRIBUTING.md` with detailed PR workflow and reviewer assignment
- GitHub Actions CI workflow for automated testing on every PR
- Troubleshooting and verification sections in `docs/customer-handover.md`

### Changed
- Restructured `mavlink_backend/` from flat scripts into a proper Python package with modules
- Updated `docker-compose.yml` to orchestrate SITL, backend, and QGC together
- Improved SITL Docker configuration for stability and faster startup
- Updated `docs/customer-handover.md` to reflect current handover state
- Updated root `README.md` with quick-start instructions and prominent links to documentation

### Fixed
- MAVLink connection handling now includes retry logic and clearer error messages
- Port references in documentation now match actual `docker-compose.yml` configuration
- Cross-references between documentation files validated and corrected

### Documentation
- [Release v0.4.0](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.4.0)
- [Sprint 4 Milestone](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/milestone/4)
- [Week 6 Report](./reports/week6/README.md)
- [Customer Handover](./docs/customer-handover.md)

## [v0.3.0] - 2026-07-03 - MVP v2 (Sprint 3)

Second MVP release with MAVLink backend and SITL integration.

### Added
- Initial `mavlink_backend/` Python scripts for MAVLink communication
- ArduPilot SITL Docker configuration (`sitl/` directory)
- `docs/customer-handover.md` (initial version)
- `docs/user-acceptance-tests.md` with basic UAT scenarios

### Changed
- Moved from manual SITL setup to Docker-based deployment
- Updated documentation structure under `docs/`

## [v0.2.0] - 2026-06-20 - Sprint 2

### Added
- Initial project structure
- Basic documentation (`README.md`, `CONTRIBUTING.md`)
- Product Backlog and Sprint Backlog setup
- Architecture documentation and first ADRs

## [v0.1.0] - 2026-06-06 - Sprint 1

### Added
- Project initialization
- Team formation and role assignment
- Initial customer meeting and requirements gathering
- First user stories and PBIs

---

[v0.5.0]: https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.5.0
[v0.4.0]: https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.4.0
[v0.3.0]: https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.3.0
[v0.2.0]: https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.2.0
[v0.1.0]: https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.1.0
