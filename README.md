# Autonomous Indoor Airship Simulation

Software Engineering course project developed for the Innopolis Robotics Lab.

The project provides a Docker-based Software-in-the-Loop (SITL) environment for an autonomous indoor airship using customized ArduPilot firmware, MAVLink communication, a FastAPI backend, and QGroundControl integration.

The final project was successfully completed during Sprint 5 (Week 7) and accepted by the customer.

---

## Project description

This project simulates an indoor airship with near-zero buoyancy using ArduPilot SITL, MAVLink, and Python backend.

---

## Final Project Status

Project status: **Completed**

The Software Engineering project has been successfully completed.

The final release includes:

- Docker-based SITL environment;
- customized ArduPilot firmware for the blimp platform;
- FastAPI MAVLink backend;
- integration with QGroundControl;
- complete project documentation;
- customer handover documentation.

The customer accepted the delivered project following the final Sprint Review.

---

## Team

- Daniyar (Product Owner)
- Arina (Scrum Master)
- Iuliana (Developer)
- Svetlana (Developer)

---

## Quick Access

### Product

- **Latest Release:** **v0.5.0 (Final MVP)**
- **Hosted Documentation:** https://innopolis-robotics-society.github.io/the_blimp_swp/

### Getting Started

- [Customer Handover](docs/customer-handover.md)
- [Launch Instructions](docs/customer-handover.md#installation-and-launch)

### Contribution

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [AGENTS.md](AGENTS.md)

### Documentation

- [Architecture](docs/architecture/README.md)
- [Testing](docs/testing.md)
- [Quality Requirements](docs/quality-requirements.md)
- [Roadmap](docs/roadmap.md)

---

## Local Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.10+
- QGroundControl

### MAVLink Backend

```bash
cd mavlink_backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python api.py
```

Backend runs on port 8000. API docs available at /docs when running.

### SITL (ArduPilot)

```bash
cd sitl
docker compose build
docker compose up sitl-auto
```

See [sitl/README.md](sitl/README.md) for details.

### Run System

1. Start SITL (above)
2. Start backend (above)
3. Connect QGroundControl to udp:127.0.0.1:14550
4. Test API via Swagger UI

### Troubleshooting

- Port in use: `docker compose down -v`
- No connection: Check SITL is running

---

## Links

### Reports
- Week 2 Report: reports/week2/README.md
- Week 3 Report: reports/week3/README.md
- Week 4 Report: reports/week4/README.md
- Week 5 Report: reports/week5/README.md
- Week 6 Report: reports/week6/README.md
- Week 7 Report: reports/week7/README.md
  
### Documentation
- Hosted Documentation: https://innopolis-robotics-society.github.io/the_blimp_swp/
- Customer Handover: docs/customer-handover.md
- Contributing: CONTRIBUTING.md
- AGENTS.md: AGENTS.md

### Technical docs
- Architecture: docs/architecture/README.md
- ADRs: docs/architecture/adr/README.md
- Development Process: docs/development-process.md
- Quality Requirements: docs/quality-requirements.md
- Quality Requirement Tests: docs/quality-requirement-tests.md
- User Acceptance Tests: docs/user-acceptance-tests.md
- Testing Strategy: docs/testing.md
- Definition of Done: docs/definition-of-done.md
- Roadmap: docs/roadmap.md

### Other
- CHANGELOG: CHANGELOG.md
- License: LICENSE

---

## License

MIT License — see LICENSE.

---

## Repository Status

This repository contains the final version of the Software Engineering course project.

All planned Sprint 5 Product Backlog Items have been completed.

The project has been delivered to the customer together with all required documentation and supporting artifacts.
