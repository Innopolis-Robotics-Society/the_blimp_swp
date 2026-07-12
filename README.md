# Autonomous Indoor Airship Simulation

A simulation environment for an autonomous near-neutral-buoyancy indoor airship (blimp), developed by **Team 19** for the **Innopolis Robotics Lab** (customer: Eugene Shlomov). The project provides a Docker-based stack combining ArduPilot SITL, a Python MAVLink backend, and QGroundControl for visualization, enabling development and testing of autonomous flight logic without physical hardware.

**Current release:** [v0.4.0 - Week 6 Trial Release](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.4.0)

---

## Team

| Name | Role | Responsibilities |
|------|------|------------------|
| Daniyar Fairushin | Product Owner | Product backlog, sprint planning, customer communication, release management |
| Arina Urakova | Scrum Master | Process facilitation, documentation, sprint coordination, Demo Day preparation |
| Iuliana Giliazutdinova | Developer | MAVLink backend, test suite, API development, CI/CD |
| Svetlana iakusheva | Developer | QGC integration, Docker configuration, infrastructure, integration testing |

---

## Quick Access

- **Hosted documentation:** https://innopolis-robotics-society.github.io/the_blimp_swp/
- **Customer handover:** [docs/customer-handover.md](./docs/customer-handover.md)
- **API documentation (Swagger UI):** http://localhost:8000/docs (after starting the stack)
- **Latest release:** [v0.4.0](https://github.com/Innopolis-Robotics-Society/the_blimp_swp/releases/tag/v0.4.0)

---

## Quick Start

### Prerequisites

- Docker and Docker Compose (v2.0+)
- Git

### Run the full stack

```bash
git clone https://github.com/Innopolis-Robotics-Society/the_blimp_swp.git
cd the_blimp_swp
docker compose up -d
```

This starts three services:

| Service | Purpose | Endpoint |
|---------|---------|----------|
| `sitl` | ArduPilot SITL simulator | UDP `127.0.0.1:14550` |
| `backend` | FastAPI MAVLink backend | http://localhost:8000 |
| `qgc` | QGroundControl visualization | Connects via Docker network |

### Verify the setup

```bash
docker compose ps
```

Then open:
- http://localhost:8000/docs - API documentation
- QGroundControl container - vehicle telemetry should appear automatically

For detailed setup, troubleshooting, and manual-start instructions, see [docs/customer-handover.md](./docs/customer-handover.md).

---

## Project Structure

```
the_blimp_swp/
├── mavlink_backend/   # Python FastAPI backend for MAVLink communication
├── sitl/              # ArduPilot SITL Docker configuration
├── QGC/               # QGroundControl Docker configuration
├── docs/              # Technical and customer-facing documentation
├── reports/           # Weekly sprint reports (Week 1 - current)
└── docker-compose.yml # Orchestrates the full stack
```

---

## Documentation

| Document | Purpose |
|----------|---------|
| [docs/customer-handover.md](./docs/customer-handover.md) | Handover state, setup, verification, troubleshooting |
| [docs/roadmap.md](./docs/roadmap.md) | Project roadmap through course completion |
| [docs/architecture/](./docs/architecture/) | System architecture and ADRs |
| [docs/user-acceptance-tests.md](./docs/user-acceptance-tests.md) | UAT scenarios and results |
| [docs/user-stories.md](./docs/user-stories.md) | User stories and acceptance criteria |
| [docs/testing.md](./docs/testing.md) | Testing strategy, coverage, and CI status |
| [docs/quality-requirements.md](./docs/quality-requirements.md) | Quality requirements (ISO/IEC 25010) |
| [docs/quality-requirement-tests.md](./docs/quality-requirement-tests.md) | Automated quality requirement tests |
| [docs/development-process.md](./docs/development-process.md) | Development workflow and git process |
| [docs/definition-of-done.md](./docs/definition-of-done.md) | Team Definition of Done |
| [CHANGELOG.md](./CHANGELOG.md) | Release history |

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- Development workflow
- PR process and reviewer assignment
- Code style and testing expectations
- Documentation standards

See [AGENTS.md](./AGENTS.md) for guidelines on AI-assisted development.

---

## Current Status

**Handover level:** Ready for independent use (pending customer confirmation)

**What works:**
- Full Docker-based deployment (SITL + backend + QGC)
- REST API for MAVLink commands and mission upload
- Automated test suite with CI/CD
- Comprehensive documentation

**Known limitations:**
- Simulation only - no physical hardware integration
- Real flight controller, UWB, and sensor integration are future work
- API endpoints have no authentication (add before production use)

See [docs/customer-handover.md](./docs/customer-handover.md) for the full list.

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
