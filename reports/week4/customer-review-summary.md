# Customer Review Summary

**Date:** 28.06.2026
**Participants:**
- Daniyar (Product Owner)
- Arina (Scrum Master)
- Iuliana (Developer)
- Svetlana (Developer)
- Eugene (Customer)

---

## Scope reviewed

- UAT scenarios (SITL startup, mission upload, telemetry in QGroundControl)
- MAVLink backend (REST API, communication logic)
- CI/CD setup (linters, Docker build, documentation)
- Simulator integration with SITL

---

## UAT results

All three UAT scenarios passed successfully:

- **UAT-01:** SITL started, heartbeat received.
- **UAT-02:** Mission uploaded, vehicle moved.
- **UAT-03:** Telemetry visible in QGroundControl.

---

## Customer feedback

- Dockerized SITL environment is already being evaluated by the client.
- Customer suggested adding Sphinx for automatic documentation builds via GitHub Pages.
- Customer confirmed that the Python simulator is enough — no need to switch to Unity.
- Customer asked the team to coordinate with the Capstone team about motor frames and flight controller setup as soon as possible.

---

## Action points

- Contact the Capstone team (Egor) about motor frames and flight controller flashing.
- Prepare a video demonstration of the simulator in the next 4 days.
- Schedule a follow-up meeting on Thursday to review progress.
- Add automatic documentation builds using Sphinx (if time permits).
