# Sprint Retrospective (Week 4)

## What went well
1. We successfully closed all Sprint 2 issues (#32–#40), including US-14 and US-22.
2. We added quality requirements and automated tests for important parts.
3. We updated the Definition of Done to include tests and coverage.
4. We created and ran UAT scenarios with the customer — all passed.
5. The customer approved our approach and confirmed no GUI or REST API is needed.
6. We created release v0.2.0 with a demo video.

## What did not go well
1. We still don't have hardware for testing — we use only SITL.
2. Some tasks (like documentation automation) were postponed due to time.

## Action points from last Sprint
1. Focus on SITL smoke-check, don't wait for hardware → **Done** (smoke-check is implemented).

## What we changed this Sprint
- We added quality requirements and automated tests for important parts.
- We updated the Definition of Done to include tests and coverage.
- We started writing and running UAT scenarios.
- We created a structured testing strategy in `docs/testing.md`.

## What we will do next Sprint
1. Coordinate with Capstone team on motor frames and flight controller setup.
2. Add automated tests for all new code (at least 30% coverage for important modules).
3. If hardware is still not ready, keep using SITL and make a backup plan.
