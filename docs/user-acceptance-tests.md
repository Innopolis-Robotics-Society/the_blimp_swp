# User Acceptance Tests

## UAT-01: Start SITL and get heartbeat

**As a** test engineer,  
**I want to** start the SITL simulation and get a MAVLink heartbeat,  
**so that** I know the simulation is ready.

**Steps:**
1. Run `./start.sh`.
2. Wait for the system to start.
3. Check the console output.

**Expected result:**
- `Heartbeat received` appears in the console.
- The system shows `Ready`.

**Status:** Pass / Fail (to be filled after UAT)

---

## UAT-02: Upload mission and fly

**As a** test engineer,  
**I want to** upload a mission with waypoints via MAVLink and start the flight,  
**so that** I can check if the autopilot follows the path.

**Steps:**
1. Load a mission file with at least 3 waypoints.
2. Upload the mission to SITL.
3. Start the simulation.

**Expected result:**
- Mission upload is accepted (`OK`).
- The vehicle starts moving to the first waypoint.
- Telemetry shows position changes.

**Status:** Pass / Fail (to be filled after UAT)

---

## UAT-03: See telemetry in QGroundControl

**As a** test engineer,  
**I want to** see telemetry (position, attitude, speed) in QGroundControl,  
**so that** I can monitor the flight.

**Steps:**
1. Start QGroundControl.
2. Connect to SITL via MAVLink.
3. Look at the telemetry fields.

**Expected result:**
- QGroundControl shows position (lat, lon, alt).
- QGroundControl shows attitude (roll, pitch, yaw).
- QGroundControl shows speed (ground speed, vertical speed).

**Status:** Pass / Fail (to be filled after UAT)
