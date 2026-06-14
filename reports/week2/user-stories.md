# User Stories

## Active stories

### US-01: Run ArduPilot SITL in Docker

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **simulation engineer**,  
I want to run ArduPilot SITL in Docker,  
so that I can test autopilot without real hardware.

**Notes:**  
- Need Docker.  
- Use official ArduPilot image.

---

### US-02: Set up MavLink communication

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **test engineer**,  
I want to set up MavLink between simulator and ground station,  
so that I can send commands and see telemetry.

**Notes:**  
- Use MavLink version 2.  
- Works with QGroundControl.

---

### US-03: Make airship follow a target

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **test engineer**,  
I want the airship to follow a target by itself,  
so that I can check if autopilot works with waypoints.

**Notes:**  
- Waypoints in Python script.  
- Need real-time position.

---

### US-04: Set up mixer for airship

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **simulation engineer**,  
I want to set up the mixer for airship,  
so that autopilot understands airship movement.

**Notes:**  
- Custom motor settings.  
- Not like quadcopter.

---

### US-05: Simple airship simulator

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **simulation engineer**,  
I want a simple airship simulator,  
so that I can test mixer and autopilot without real hardware.

**Notes:**  
- Simple physics: mass, buoyancy, thrust.  
- Python.

---

### US-06: Connect RC transmitter

**Requirement status:** Active  
**MoSCoW priority:** Should Have  

As a **test engineer**,  
I want to connect RC transmitter via Wi-Fi,  
so that I can manually control the airship if needed.

**Notes:**  
- ELRS protocol.  
- Manual control works anytime.

---

### US-07: See telemetry on screen

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **test engineer**,  
I want to see telemetry (position, speed, direction),  
so that I can find problems in autopilot.

**Notes:**  
- Real-time or print to terminal.  
- Text output is fine.

---

### US-08: Control flight speed and height

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **test engineer**,  
I want to change the airship speed and height during flight,  
so that I can test how autopilot reacts to different conditions.

**Notes:**  
- Change speed (0 to max).  
- Change height (low to high).  
- Must work in real time.

---

### US-09: Safe mode when connection lost

**Requirement status:** Active  
**MoSCoW priority:** Should Have  

As a **test engineer**,  
I want autopilot to go to safe mode if connection is lost,  
so that the airship does not fly badly.

**Notes:**  
- Go to loiter or land mode.  
- Recover when connection is back.

---

### US-10: Take off and landing control

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **flight operator**,  
I want to control take off and landing of the airship,  
so that I can safely start and finish the flight.

**Notes:**  
- One button for take off.  
- One button for landing.  
- Works in simulation and with real airship.

---

### US-11: Send real-time position from simulator

**Requirement status:** Active  
**MoSCoW priority:** Must Have  

As a **test engineer**,  
I want the simulator to send real-time position,  
so that I can check if the airship follows the path correctly.

**Notes:**  
- Send x, y, z, yaw 10 times per second.  
- Needed for US-03.

---

## Removed stories

### US-12: Voice control for airship

**Requirement status:** Removed  
**Previous MoSCoW priority:** Could Have  

As a **test engineer**,  
I want to control the airship with voice,  
so that I can test hands-free.

**Reason:**  
Customer said no. No one asked for this.

---

### US-13: Mobile app for telemetry

**Requirement status:** Removed  
**Previous MoSCoW priority:** Could Have  

As a **test engineer**,  
I want to see telemetry on my phone,  
so that I can watch the airship from anywhere.

**Reason:**  
Out of scope. No time for mobile app. Customer agreed.

---

## Initial proposed MVP v1 scope

- US-01: Run ArduPilot SITL in Docker
- US-02: Set up MavLink communication
- US-05: Simple airship simulator
- US-07: See telemetry on screen
- US-11: Send real-time position from simulator
