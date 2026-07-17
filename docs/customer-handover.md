# Customer Handover

**Project:** Autonomous Indoor Airship Simulation  
**Team:** 19  
**Customer:** Eugene Shlomov (Innopolis Robotics Lab)  
**Release:** v0.5.0 (MVP v3)  
**Date:** 17.07.2026

---

# Handover Level

- [x] Ready for independent use
- [x] Independently used by customer
- [x] Deployed or operated on customer side

# Customer Confirmation Status

- [x] Accepted
- [ ] Accepted with follow-up items
- [ ] Not yet accepted

The project was accepted during the final Sprint Review following the demonstration of the completed MVP and the project documentation.

---

# Purpose

This document records the formal transfer of the Autonomous Indoor Airship Simulation project to the customer after completion of the Software Engineering course.

The repository now contains the complete implementation, documentation, and supporting materials required to deploy, understand, maintain, and further extend the project.

---

# Delivered Assets

The following project assets have been transferred.

| Item | Status | Notes |
|------|--------|-------|
| Source code repository | Transferred | Complete Git history and project files |
| Docker-based SITL environment | Transferred | Simulation environment |
| MAVLink backend | Transferred | FastAPI backend |
| QGroundControl configuration | Transferred | Repository configuration and usage instructions |
| Documentation | Transferred | Technical and development documentation |
| Architecture documentation | Transferred | Static, dynamic and deployment views |
| Architecture Decision Records | Transferred | Design decisions documented throughout the project |
| Quality documentation | Transferred | Quality requirements, tests and UAT |
| Sprint reports | Transferred | Weekly reports and project documentation |
| GitHub Actions workflows | Transferred | CI/CD configuration |

The repository contains all artifacts produced during the project. No additional project materials are maintained separately.

---

# Responsibilities After Handover

Following customer acceptance, responsibility for future maintenance and development is transferred to the customer.

The delivered repository provides:

- complete source code;
- project documentation;
- deployment instructions;
- development history;
- testing artifacts;
- architecture documentation.

The project team remains available during the course completion period for clarification of the delivered documentation if required.

---

# Repository Structure

The customer receives the complete repository.

```text
.
├── .github/
├── docs/
│   ├── architecture/
│   ├── customer-handover.md
│   ├── development-process.md
│   ├── interface.md
│   ├── quality-requirements.md
│   ├── quality-requirement-tests.md
│   ├── roadmap.md
│   ├── testing.md
│   └── user-acceptance-tests.md
├── mavlink_backend/
├── QGC/
├── reports/
├── sitl/
├── AGENTS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

# Environment Requirements

The project was developed and tested on Ubuntu 22.04 LTS.

Required software:

- Docker
- Docker Compose
- Python 3.10+
- Git
- QGroundControl

For deployment on the physical platform:

- MAVLink-compatible flight controller
- Airship running the customized ArduMotorBlimp firmware

---

# Configuration

The default configuration is sufficient for running the delivered system.

| Variable | Default |
|----------|---------|
| `MAVLINK_CONNECTION` | `udp:127.0.0.1:14550` |
| `FASTAPI_HOST` | `0.0.0.0` |
| `FASTAPI_PORT` | `8000` |

No secrets, authentication keys, or external services are required for normal operation.

---

# Deployment

Clone the repository.

```bash
git clone https://github.com/Innopolis-Robotics-Society/the_blimp_swp.git
cd the_blimp_swp
```

Start the simulation environment.

```bash
cd sitl
docker compose up -d
```

Start the backend.

```bash
cd ../mavlink_backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python api.py
```

The REST API becomes available at

```text
http://localhost:8000/docs
```

Launch QGroundControl and connect to the default MAVLink endpoint.

```text
udp://127.0.0.1:14550
```

The system is ready once telemetry is visible in QGroundControl and the backend reports an active MAVLink connection.

---

# Verification

Before handover the following functionality was verified.

| Component | Status |
|----------|--------|
| Docker environment | Verified |
| SITL | Verified |
| MAVLink backend | Verified |
| REST API | Verified |
| QGroundControl communication | Verified |
| Ground-to-airship MAVLink communication | Verified |
| Customized firmware deployment | Verified |

---

# Documentation Entry Points

The repository contains all documentation required to understand, deploy, maintain, and further develop the project.

The primary documentation entry points are listed below.

| Location | Description |
|----------|-------------|
| `README.md` | Project overview, prerequisites, installation, and quick start |
| `CHANGELOG.md` | Release history |
| `CONTRIBUTING.md` | Contribution workflow and development guidelines |
| `AGENTS.md` | Development guidelines used during the project |
| `docs/architecture/README.md` | Architecture documentation index |
| `docs/architecture/adr/README.md` | Architecture Decision Records |
| `docs/development-process.md` | Software development workflow |
| `docs/interface.md` | System interfaces and component communication |
| `docs/testing.md` | Testing strategy and testing process |
| `docs/quality-requirements.md` | Functional and non-functional quality requirements |
| `docs/quality-requirement-tests.md` | Verification of quality requirements |
| `docs/user-acceptance-tests.md` | User acceptance testing scenarios |
| `docs/roadmap.md` | Project roadmap |
| `reports/` | Sprint reports, reflections, retrospectives and supporting project documentation |

All project artifacts developed during the Software Engineering course are stored within the repository.

---

# Customer Acceptance

The final Sprint Review included a demonstration of the completed project, documentation walkthrough, and discussion of the delivered functionality.

During the review, the customer confirmed that:

- the agreed project objectives had been achieved;
- the delivered software satisfies the defined project scope;
- the documentation is sufficient for understanding and continuing development of the project;
- the repository contains the required implementation and supporting documentation.

Following the review, the project was accepted as the final course deliverable.

---

# Known Limitations

The project successfully satisfies the objectives defined for the Software Engineering course. Some improvements remain possible for future development.

Current limitations include:

- UWB-based localization has not yet been integrated into the complete navigation workflow.
- Autonomous navigation algorithms require additional validation on the physical platform.
- Extended long-duration testing on the real airship was outside the scope of the course.
- Future hardware revisions may require additional firmware configuration.

These limitations were communicated during the final project review.

---

# Recommendations for Future Development

The delivered repository provides a solid foundation for future work.

Potential development directions include:

- integration of UWB localization into autonomous flight;
- improved autonomous navigation algorithms;
- obstacle detection and avoidance;
- support for additional onboard sensors;
- extended mission planning capabilities;
- additional validation on the physical platform;
- optimization of backend services and monitoring tools.

The current project architecture allows these improvements to be implemented incrementally without significant restructuring.

---

# Support

The complete project history, implementation, and documentation are available in the project repository.

Future developers should begin with:

1. `README.md`
2. `docs/architecture/README.md`
3. `docs/development-process.md`
4. `docs/interface.md`

Questions regarding implementation details can be answered by consulting the architecture documentation, Architecture Decision Records, and sprint reports included in the repository.

---

# Handover Summary

The Autonomous Indoor Airship Simulation project has been successfully completed and transferred to the customer.

The delivered repository includes:

- complete source code;
- simulation environment;
- MAVLink backend;
- customized firmware configuration;
- project documentation;
- architecture documentation;
- quality assurance artifacts;
- sprint reports and development history.

The project was demonstrated during the final Sprint Review and accepted by the customer.

Responsibility for future maintenance, feature development, and further research is transferred to the customer.

This document concludes the project handover and marks the completion of the Software Engineering project.

---

## Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 12.07.2026 | Initial handover draft prepared before customer review |
| 1.0 | 17.07.2026 | Final version following customer acceptance and project completion |
