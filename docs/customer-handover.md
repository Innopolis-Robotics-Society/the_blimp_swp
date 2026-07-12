# Customer Handover

**Project:** Autonomous Indoor Airship Simulation  
**Team:** 19  
**Customer:** Eugene Shlomov (Innopolis Robotics Lab)  
**Date:** 12.07.2026

---

## Handover Level

- [x] Ready for independent use
- [ ] Independently used by customer
- [ ] Deployed or operated on customer side

## Customer Confirmation Status

- [ ] Accepted
- [ ] Accepted with follow-up items
- [ ] Not yet accepted (meeting pending)

---

## What is Being Transferred

| Item | Status | Notes |
|------|--------|-------|
| Source code repository | Transferred | Full GitHub repository access |
| Dockerized SITL environment | Transferred | ArduPilot simulation container |
| QGroundControl in Docker | Transferred | Visualization tool containerized |
| MAVLink Python backend | Transferred | FastAPI-based API for vehicle control |
| Documentation suite | Transferred | Both repo-resident and hosted docs |
| Architecture docs and ADRs | Transferred | Technical decision records included |
| Test suite | Transferred | Unit, integration, and quality tests |
| CI/CD pipeline | Transferred | GitHub Actions workflows |
| Deployment instructions | Transferred | Complete setup and run guide |

## What Was Delegated

- Ongoing maintenance and bug fixes after course completion
- Future feature development based on lab needs
- Documentation updates as the project evolves
- Issue tracking and resolution through GitHub

## What Was Retained by the Team

- Active development support until end of course (Week 8 Demo Day)
- Final delivery of MVP v3 release
- Knowledge transfer sessions with the lab team

---

## Environment Variables and Configuration

The project uses the following configuration values:

| Variable | Default | Description | Required |
|----------|---------|-------------|----------|
| `MAVLINK_CONNECTION` | `udp:127.0.0.1:14550` | Connection string for MAVLink | Yes |
| `FASTAPI_HOST` | `0.0.0.0` | Backend API host | No |
| `FASTAPI_PORT` | `8000` | Backend API port | No |

**Note:** No sensitive secrets, API keys, or credentials are required for basic operation. All configuration can be modified in `docker-compose.yml` and `.env` files if needed.

---

## Setup, Deployment, and Verification

### Prerequisites

- Docker and Docker Compose (v2.0+)
- Python 3.10+ (for local backend development)
- Git
- QGroundControl (optional - also available in Docker)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Innopolis-Robotics-Society/the_blimp_swp.git
   cd the_blimp_swp
   ```

2. **Start all services with Docker Compose:**
   ```bash
   docker compose up -d
   ```

3. **Verify the setup:**
   - SITL container is running: `docker compose ps`
   - Backend API accessible: http://localhost:8000/docs
   - QGroundControl connects to the vehicle (either Docker or local installation)

### Manual Start (Alternative)

If you prefer to run components separately:

1. **Start SITL:**
   ```bash
   cd sitl
   docker compose up -d
   ```

2. **Start backend:**
   ```bash
   cd mavlink_backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python api.py
   ```

3. **Start QGroundControl:**
   - Use the Docker container, OR
   - Install locally from [QGroundControl](https://qgroundcontrol.com) and connect to `udp://127.0.0.1:14550`

### Recovery and Troubleshooting

| Problem | Solution |
|---------|----------|
| SITL container fails to start | Check Docker logs: `docker compose logs sitl` |
| Backend won't start | Ensure port 8000 is not in use; check `python --version` |
| QGroundControl won't connect | Verify UDP port 14550 is accessible; restart containers |
| Mission upload fails | Check MAVLink connection in Swagger UI at `/docs` |
| Vehicle not appearing | Wait 30-60 seconds after SITL startup for full initialization |

For more troubleshooting steps, see [docs/troubleshooting.md](./troubleshooting.md) if available, or open an issue in the repository.

---

## Documentation Entry Points

The documentation is organized as follows:

### For Normal Operation
- **[README.md](../README.md)** - Main project overview and quick start
- **[Hosted Documentation](https://innopolis-robotics-society.github.io/the_blimp_swp/)** - Full online docs with search
- **[API Documentation](http://localhost:8000/docs)** - Swagger UI for backend endpoints

### For Development
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - How to contribute code and documentation
- **[AGENTS.md](../AGENTS.md)** - Guidelines for AI agent usage
- **[docs/architecture/](./architecture/)** - System architecture and design decisions (ADRs)

### For Troubleshooting
- **[CHANGELOG.md](../CHANGELOG.md)** - Release notes and version history
- **GitHub Issues** - Known bugs and feature requests
- **GitHub Discussions** - Community support and questions

---

## Is the Documentation Sufficient?

### What's Complete
Complete setup and deployment guide  
API documentation with Swagger UI  
Architecture and design decision records  
Testing strategy and test suite  
Contributing guidelines  
CI/CD pipeline documentation  

### What's Still Needed
Final customer validation after trial release (pending meeting)  
Hardware integration documentation (future work)  
UWB localization expansion docs (future work)  

### Support Required
The project is ready for independent use with current documentation. The team remains available for:
- Answering questions during the transition period
- Final knowledge transfer sessions
- Bug fixes identified during customer trial
- Final delivery of MVP v3 in Week 7

---

## Known Limitations

1. **Simulation Only:** This release uses ArduPilot SITL - no physical hardware integration yet
2. **Limited Hardware Support:** Real flight controller, UWB, and sensor integration are not implemented
3. **Windows Compatibility:** Docker-based approach works best on Linux/macOS; Windows may require WSL2
4. **Network Requirements:** All components communicate over UDP - ensure no firewall blocks port 14550
5. **No Authentication:** API endpoints are open - add authentication before production use

---

## Future Roadmap (Post-Handover)

Based on customer needs and project goals, future work may include:

1. **Physical Hardware Integration**
   - Real ArduPilot flight controller connection
   - UWB positioning system integration
   - Sensor data processing (IMU, cameras)

2. **Advanced Autonomy**
   - Improved path planning algorithms
   - Obstacle detection and avoidance
   - Multi-agent coordination

3. **Enhanced Visualization**
   - Real-time telemetry dashboards
   - Web-based control interface
   - 3D environment mapping

4. **Production Readiness**
   - User authentication and authorization
   - Comprehensive error handling and recovery
   - Performance optimization for multiple vehicles

---

## Contact Information

**During the course:**  
Use GitHub Issues, PRs, or Discussions for all project-related questions.

**After course completion:**  
Contact Innopolis Robotics Lab team members for ongoing support.

**Documentation updates:**  
All documentation lives in this repository. Updates can be submitted via PR following [CONTRIBUTING.md](../CONTRIBUTING.md).
