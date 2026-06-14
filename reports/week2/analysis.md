# Week 2 Analysis

## Learning points

- We learned that standard assignment requirements (Figma, Swagger, cloud deployment) are made for web apps. For our robotics project, they do not fit directly, but we can adapt them.

- We learned how to write user stories for an engineering system. Instead of "buttons", we described MAVLink commands, localization, and telemetry.

- MoSCoW helped us separate what is important (Must Have) from what is less important (Should Have, Could Have). We selected 8 Must Have stories for MVP v1.

- We learned that MVP for robotics is not a website on Vercel. It is a working simulation (SITL) where a virtual airship receives commands and sends telemetry.

## Validated assumptions

- Assumption: we need a Figma prototype. → Rejected. Customer confirmed that QGroundControl and MAVLink documentation are fine.

- Assumption: we need REST API and Swagger. → Partially confirmed. We have a REST API (backend on Raspberry Pi), but we do not make Swagger. Instead we have `docs/interface.md`.

- Assumption: video must show a real airship. → Rejected. Physical airship is not ready until July–August. We show SITL simulation.

- Assumption: MVP must be deployed online. → Rejected. The system runs locally using Docker and SITL.

## Needs clarification

- How exactly do we check that EKF3 works correctly with UWB data? (We will test in SITL with real UWB logs.)

- Who provides the hardware for field tests? (Customer or lab?)

- What is the exact metric for "successful trajectory tracking"? (For example, max deviation 10 cm?)

- Can we pass the smoke-check without a video? (We agreed with TA that no video is needed, we can show live demo on request.)

## Planned response

- MVP v1 will be implemented in SITL first, then moved to real hardware.

- Instead of Figma, we will create `docs/interface.md` with MAVLink and CLI description.

- Smoke-check will be automated with a Python script: check heartbeat, mission upload, telemetry update.

- We do not record a video, but if the instructor asks, we can show the simulation live.
