# MVP v0 Report

## Purpose and Description

MVP v0 demonstrates the current software components of the Autonomous Indoor Airship Simulation project in the ArduPilot SITL environment.

The current implementation focuses on simulation, backend functionality, and communication between system components. The physical airship is not yet available.

## Deployment

The project is not deployed online. It is intended to run locally using ArduPilot SITL together with the project backend.

## Video Demonstration

No public video is provided for Week 2 because the current SITL implementation does not represent the final robotics system.

If requested by the instructors or the customer, the team can demonstrate the current implementation live.

## Relationship to Prototype and MVP v1

MVP v0 validates the software architecture and communication in simulation. Future versions will extend this functionality and integrate with the physical platform.

## Limitations

* Development is currently performed in simulation.
* The physical airship platform is still under construction.
* Hardware integration has not yet been completed.

## Local Setup

1. Install the required dependencies.
2. Start the ArduPilot SITL simulation.
3. Start the project backend.
4. Verify communication between components.

Detailed instructions are available in the repository documentation.

## Smoke-Check Scenario

The smoke check is successful if:

1. The SITL environment starts correctly.
2. A MAVLink heartbeat is received.
3. Communication between components is established.
4. Telemetry is received and updates correctly.
