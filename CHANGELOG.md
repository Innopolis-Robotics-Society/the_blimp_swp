# Changelog

## [v0.3.0] - 2026-07-05
### Added
- Architecture documentation (static, dynamic, deployment views)
- 3 ADRs (Architecture Decision Records)
- Development process documentation with Mermaid diagram
- MVP v2 implementation
- 2 new UAT scenarios (UAT-04, UAT-05)

### Changed
- Updated roadmap with Sprint 3 completion
- Updated quality requirements with links to ADRs
- Removed Windows instructions from documentation (customer feedback)

### Fixed
- No critical issues reported

---

## [v0.2.0] - 2026-06-28
### Added
- Quality requirements (QR-01, QR-02, QR-03) with ISO/IEC 25010 sub-characteristics
- Automated quality requirement tests (QRT-01, QRT-02, QRT-03)
- UAT scenarios (UAT-01, UAT-02, UAT-03)
- Updated Definition of Done with tests and coverage
- Testing strategy documentation (`docs/testing.md`)
- CI configuration for automated test execution
- MAVLink backend with REST API and WebSocket
- Integration tests with SITL
- Local setup instructions in README

### Changed
- All Sprint 2 issues (#32–#40) are closed
- Updated root README.md with local setup instructions

### Fixed
- No critical issues reported

---

### Added
- SITL ArduPilot Blimp runs in Docker
- MAVLink connection with QGroundControl
- Telemetry streaming (position, attitude, velocity)
- Mission upload via MAVLink
- Startup script for SITL + backend
- Arming and disarming via MAVLink
- Flight mode switching (Loiter, Guided, RTL)
- Parameter read and write via MAVLink
- Flight log recording
- Fail‑safe mode on MAVLink connection loss

### Fixed
- No critical issues reported

---

## [v0.1.0] - 2026-06-20
### Added
- First MVP v1 release
- Core SITL simulation with MAVLink communication
- Basic telemetry and mission upload
