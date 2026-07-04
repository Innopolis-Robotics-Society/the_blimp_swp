# User Acceptance Tests

## UAT-01: Setup, container launch and basic connection (Smoke test)

**Goal:** Make sure the user can run the Docker container, open QGroundControl, and see telemetry from the connected (virtual) vehicle.

**Preconditions:**
- Docker is installed on the user's machine.
- No physical drone is connected (SITL simulator is used).
- Setup instructions are available.

**Steps:**
1. Clone the repository: `git clone https://github.com/Innopolis-Robotics-Society/the_blimp_swp.git`
2. If using WSL, switch to the WSL branch: `git checkout fix/wsl-sitl-latest`
3. Run the Docker container using the instructions in `sitl/README.md#quickstart` (use Auto-start for quick testing).
4. Wait for the container to reach `Up` status.
5. Open QGroundControl.
6. Go to the **Fly** tab.
7. Check that telemetry widgets are visible (altitude, speed, battery, GPS status).
8. Click the **Arm** button (or check the readiness status).

**Expected result:**
- Container starts without critical errors (no `panic` or `fatal error` in logs).
- The Fly tab shows a connected vehicle.
- Telemetry widgets show real values. GPS indicator shows satellite lock.
- UAT-01 passed.

---

## UAT-02: Mission planning, upload and autonomous flight

**Goal:** Check two-way communication between QGC and the backend (simulator), and verify that the mission planning module works correctly.

**Preconditions:**
- UAT-01 passed. Vehicle is connected and visible in QGC.

**Steps:**
1. Go to the **Plan** tab.
2. Add at least 3–4 waypoints on the map to create a simple route (e.g., a square).
3. Set a safe altitude for each waypoint (e.g., 10–15 meters).
4. Click **Upload** to send the mission to the vehicle.
5. Go to the **Fly** tab.
6. Arm the motors.
7. Switch the flight mode to **Auto** or **Mission**.
8. Watch the drone marker move on the map and telemetry change.
9. Wait for all waypoints to be completed and the vehicle to return or land (or cancel with RTL / Return).

**Expected result:**
- Mission is built successfully in the editor.
- Upload shows a confirmation message (`Mission uploaded`).
- After switching to Auto mode, the virtual drone starts moving through the waypoints.
- The map marker is synchronized with the actual (virtual) position.
- Telemetry (altitude, distance to home) updates in real time.
- UAT-02 passed.

---

## UAT-03: Parameter change and pre-arm safety check

**Goal:** Make sure the user can change vehicle parameters through QGC, save them, and use standard safety checklists.

**Preconditions:**
- UAT-01 passed. Vehicle is connected.

**Steps:**
1. Go to **Vehicle Setup** (gear icon or 'Q' in the top left).
2. Select the **Parameters** tab.
3. Search for a safe parameter, e.g., `RTL_ALT` (return altitude) or `BRD_SAFETY_DEFLT`.
4. Change the value (e.g., set `RTL_ALT` from 1500 to 2000).
5. Click **Save** and confirm any restart if prompted.
6. Wait for the vehicle to reconnect.
7. Go to the **Summary** or **Pre-flight** check section (if enabled).
8. Return to the **Fly** tab and try to arm the motors without calibration or checks (e.g., right after SITL restart, before GPS is ready).

**Expected result:**
- Parameter list loads without interface freezing.
- The new value is saved and applied successfully.
- QGC responds correctly: if the vehicle is not ready (e.g., compass/gyro not passed in SITL), QGC shows a clear warning (`Pre-arm safety check failed`) and prevents arming.
- UAT-03 passed.

---

## UAT-04: Run Dockerized SITL on Linux

**Goal:** Make sure the user can run the Dockerized SITL environment on Linux without additional configuration.

**Preconditions:**
- Linux OS (Ubuntu 22.04+)
- Docker and Docker Compose installed
- Repository cloned

**Steps:**
1. Clone the repository.
2. Run `docker compose up` in the `sitl/` folder.
3. Wait for the container to start.
4. Open QGroundControl.
5. Connect to `udp:127.0.0.1:14550`.

**Expected result:**
- Container starts without errors.
- QGroundControl shows a connected vehicle.
- Telemetry is visible.

**Status:** Passed (customer confirmed during Sprint Review)

---

## UAT-05: Custom ArduPilot vehicle build

**Goal:** Verify that the custom ArduPilot vehicle (ArduMotorBlimp) can be built and configured.

**Preconditions:**
- Linux OS
- ArduPilot build environment set up
- Custom vehicle files in place

**Steps:**
1. Run `./waf configure --board sitl`.
2. Run `./waf build --vehicle ArduMotorBlimp`.
3. Check build output for errors.
4. Run the built vehicle in SITL.

**Expected result:**
- Build completes without errors.
- SITL starts with the custom vehicle.
- Vehicle responds to MAVLink commands.

**Status:** Passed (customer confirmed during Sprint Review)
