# Quality Requirements

## QR-01: MAVLink message speed

**ISO/IEC 25010 sub-characteristic:** Performance Efficiency — Time Behaviour  
**Why it matters:** The system must process MAVLink messages fast enough to keep the airship stable and show telemetry in real time.  
**What we check:** When the system gets a MAVLink heartbeat, it must parse and save it within **50 ms** on a Raspberry Pi 4 (or similar hardware).  
**How we test:** QRT-01 runs automatically in CI. It sends 100 messages and checks the average time. If it is over 50 ms, the test fails.  
**Related stories:** US-12, US-15, US-21.

---

## QR-02: SITL stability

**ISO/IEC 25010 sub-characteristic:** Reliability — Maturity  
**Why it matters:** The simulation must not crash during tests or demos.  
**What we check:** The system runs a 5-minute mission with at least 3 waypoints and MAVLink connection. No crashes or errors are allowed.  
**How we test:** QRT-02 runs this mission in CI. If the simulation crashes or shows an error, the test fails.  
**Related stories:** US-12, US-13, US-21.

---

## QR-03: Telemetry update rate

**ISO/IEC 25010 sub-characteristic:** Performance Efficiency — Resource Utilization  
**Why it matters:** Telemetry must update often enough for safe manual control and good logging.  
**What we check:** The system must send telemetry (position, attitude, velocity) at least **10 times per second** during simulation.  
**How we test:** QRT-03 checks the telemetry stream. If the average rate is below 10 Hz, the test fails.  
**Related stories:** US-15.
