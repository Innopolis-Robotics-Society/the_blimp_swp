# Sprint Retrospective (Week 4)

## What went well
1. We finished all Must Have tasks for MVP v1 and made SITL work with MAVLink, mission upload, and telemetry.
2. The customer said our approach is good and we don't need a GUI or REST API.
3. We added technical tasks to the backlog (Docker, startup script, QGC integration).

## What did not go well
1. We don't have hardware for testing — we use only SITL.
2. US-14 (UWB) and US-22 (smoke-check) are not done and moved to the next Sprint.

## Action points from last Sprint
1. Ask others to create Projects → **Done** (projects are created now).
2. Focus on SITL smoke-check, don't wait for hardware → **Partly done** (smoke-check still in progress).

## What we changed this Sprint
- We added quality requirements and automated tests for important parts.
- We updated the Definition of Done to include tests and coverage.
- We started writing UAT scenarios.

## What we will do next Sprint
1. Add automated tests for all new code (at least 30% coverage for important modules).
2. Finish US-14 (UWB) and US-22 (smoke-check).
3. If hardware is still not ready, keep using SITL and make a backup plan.
