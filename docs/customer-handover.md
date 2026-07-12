# Customer Handover

**Project:** Autonomous Indoor Airship Simulation  
**Team:** 19  
**Customer:** Eugene Shlomov (Innopolis Robotics Lab)  
**Date:** 12.07.2026

---

## Handover level

- [x] Ready for independent use
- [ ] Independently used by customer
- [ ] Deployed or operated on customer side

## Customer confirmation status

- [ ] Accepted
- [ ] Accepted with follow-up items
- [ ] Not yet accepted

---

## What is being transferred

- Source code repository: [the_blimp_swp](https://github.com/Innopolis-Robotics-Society/the_blimp_swp)
- Documentation: [Hosted docs](https://innopolis-robotics-society.github.io/the_blimp_swp/)
- Architecture documentation and ADRs
- Quality requirements and tests
- CI/CD pipeline
- Dockerized SITL environment

---

## Access instructions

### Prerequisites

- Docker and Docker Compose
- Python 3.10+
- QGroundControl

### Clone the repository

```bash
git clone https://github.com/Innopolis-Robotics-Society/the_blimp_swp.git
cd the_blimp_swp
```

### Start SITL

```bash
cd sitl
docker compose up -d
```

### Start backend

```bash
cd mavlink_backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python api.py
```
### Connect QGroundControl
Connect to udp://127.0.0.1:14550.

### API documentation
Swagger UI is available at http://localhost:8000/docs.

---

### Configuration
No environment variables or secrets are required for local development.

---

### Known limitations

- No physical hardware integration yet (UWB, flight controller).
- SITL simulation only (no real airship).
- Windows support is not guaranteed (use Linux).

---

### Support after handover
- Documentation is available in the repository and hosted docs.
- For questions, contact the team via the repository or the Innopolis Robotics Lab chat.

---

### Verification steps
**To verify the system works:**
- Start SITL and backend.
- Open QGroundControl – you should see a connected vehicle.
- Upload a mission via Swagger UI or QGroundControl.
- Switch to Auto mode – the vehicle should move.

---

### Next steps
- Integrate with real hardware.
- Expand UWB localization.
- Improve autonomous navigation.
