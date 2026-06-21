# Customer Review Summary

## Date
21.06.2026

## Participants
- Daniyar (Product Owner)
- Arina (Scrum Master)
- Iuliana (Developer)
- Svetlana (Developer)
- Eugene (customer)

## Scope reviewed
- SITL running in Docker container
- Airship physics simulator in Python (under review)
- MAVLink connection between Raspberry Pi and flight controller via ELRS Backpack
- Custom scripts and parameters for vehicle configuration
- QGroundControl integration (planned)

## Feedback
- Customer is satisfied with the progress.
- Python-based simulator with Matplotlib visualization is sufficient; no need to switch to Unity.
- Customer wants to see the simulator after the meeting.
- QGroundControl should be included in the Docker container in the future.

## Approvals
- Current approach and progress are approved.
- Customer agrees to continue with Python development.
- Option to modify ArduPilot source code is postponed until a separate in-person meeting.

## Action points
- Send the simulator link to Eugene.
- Continue integrating the physics simulator with SITL.
- Test the full connection (Raspberry Pi → LRS → flight controller) when the RC transmitter arrives.
- Consider adding QGroundControl to the Docker package.
- If ArduPilot modifications are needed, arrange a separate meeting.
