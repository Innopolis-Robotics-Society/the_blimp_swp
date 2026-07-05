# the_blimp_swp

The repo assigned to SWP Team.
Autonomous Indoor Airship Simulation — SWP course project.

## Project description

This project simulates an indoor airship with near-zero buoyancy using ArduPilot SITL, MAVLink, and Python backend.

---

## Team
- Daniyar (Product Owner)
- Arina (Scrum Master)
- Iuliana (Developer)
- Svetlana (Developer)

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

Backend runs on port 8000.
API docs available at /docs when running.

### SITL (ArduPilot)

```bash
cd sitl
docker build -t ardupilot-sitl .
docker run -d --name sitl -p 14550:14550/udp ardupilot-sitl
```

### Run System

1. Start SITL (above)
2. Start backend (above)
3. Connect QGroundControl to udp:127.0.0.1:14550
4. Test API via Swagger UI

### Troubleshooting

- Port in use: docker stop sitl && docker rm sitl
- No connection: Check SITL is running

---

## Links
- [Week 2 Report](reports/week2/README.md)
- [Week 3 Report](reports/week3/README.md)
- [Week 4 Report](reports/week4/README.md)
- [Week 5 Report](reports/week5/README.md)
- [Quality Requirements](docs/quality-requirements.md)
- [Quality Requirement Tests](docs/quality-requirement-tests.md)
- [User Acceptance Tests](docs/user-acceptance-tests.md)
- [Testing Strategy](docs/testing.md)
- [Definition of Done](docs/definition-of-done.md)
- [Roadmap](docs/roadmap.md)
- [CHANGELOG](CHANGELOG.md)
- [Architecture](docs/architecture/README.md)
- [ADRs](docs/architecture/adr/)
- [Development Process](docs/development-process.md)
- [Hosted Documentation](https://innopolis-robotics-society.github.io/the_blimp_swp/)

---

## License
MIT License — see [LICENSE](LICENSE).
