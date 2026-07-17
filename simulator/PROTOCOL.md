# Blimp Physics Engine — Input/Output Protocol

## Overview

The simulator communicates with ArduPilot SITL over UDP using the **SIM_JSON** protocol:
- **Input**: binary servo packet from ArduPilot (motor PWM values)
- **Output**: JSON sensor data to ArduPilot (IMU, position, velocity, attitude)

Default port: `9002/udp` on `127.0.0.1`

---

## Input: Servo Packet (ArduPilot → Simulator)

Binary UDP packet with PWM motor outputs.

### 16-channel format (magic = `0x481A` = 18458)

| Offset | Size      | Field       | Description                   |
|--------|-----------|-------------|-------------------------------|
| 0      | 2 (uint16)| magic       | `18458`                       |
| 2      | 2 (uint16)| frame_rate  | Desired frame rate (Hz)       |
| 4      | 4 (uint32)| frame_count | Frame counter                 |
| 8      | 32        | pwm[16]     | PWM values, channels 0–15     |

Total: 40 bytes

### 32-channel format (magic = `0x7381` = 29569)

| Offset | Size      | Field       | Description                   |
|--------|-----------|-------------|-------------------------------|
| 0      | 2 (uint16)| magic       | `29569`                       |
| 2      | 2 (uint16)| frame_rate  | Desired frame rate (Hz)       |
| 4      | 4 (uint32)| frame_count | Frame counter                 |
| 8      | 64        | pwm[32]     | PWM values, channels 0–31     |

Total: 72 bytes

All fields are **little-endian**.

### PWM to Thrust Conversion

```
normalized = (pwm_value - 1000) / 1000.0
```

| PWM  | Normalized | Meaning   |
|------|-----------|-----------|
| 1000 | 0.0       | Off       |
| 1500 | 0.5       | 50%       |
| 2000 | 1.0       | Max       |

Clamped to [0.0, 1.0].

### Default Motor Mapping

| Channel | Motor | Direction (body NED) | Purpose    |
|---------|-------|---------------------|------------|
| 0       | M1    | [+1, 0, 0]          | Forward    |
| 1       | M2    | [-1, 0, 0]          | Backward   |
| 2       | M3    | [0, 0, -1]          | Lift       |
| 3       | M4    | [0, +1, 0]          | Yaw/strafe |

---

## Output: JSON Sensor Data (Simulator → ArduPilot)

Plain text JSON terminated by `\n`.

### Required Fields

```json
{
  "timestamp": 1.234567,
  "imu": {
    "gyro": [0.001, -0.002, 0.003],
    "accel_body": [0.1, 0.2, 9.81]
  },
  "velocity": [0.5, 0.0, -0.1],
  "quaternion": [0.999, 0.0, 0.0, 0.01]
}
```

### Optional Fields

```json
{
  "position": [1.0, 2.0, -0.5],
  "latitude": 47.9945,
  "longitude": 55.9638,
  "altitude": 0.5,
  "no_time_sync": true,
  "no_lockstep": true
}
```

### Field Reference

| Field              | Type    | Unit   | Frame      | Description                           |
|--------------------|---------|--------|------------|---------------------------------------|
| `timestamp`        | double  | s      | —          | Simulation time                       |
| `imu.gyro`         | float×3 | rad/s  | body NED   | Angular velocity `[x, y, z]`          |
| `imu.accel_body`   | float×3 | m/s²   | body NED   | Acceleration `[x, y, z]`              |
| `velocity`         | float×3 | m/s    | earth NED  | `[North, East, Down]`                 |
| `quaternion`       | float×4 | —      | —          | Attitude `[w, x, y, z]` Hamilton      |
| `position`         | float×3 | m      | earth NED  | Relative to home `[N, E, D]`          |
| `latitude`         | double  | deg    | —          | WGS84 latitude                        |
| `longitude`        | double  | deg    | —          | WGS84 longitude                       |
| `altitude`         | float   | m      | —          | Altitude above home                   |
| `no_time_sync`     | bool    | —      | —          | Skip time sync with SITL              |
| `no_lockstep`      | bool    | —      | —          | Run without lockstep                  |

### Coordinate Frames

**Body NED**: X — forward, Y — right, D — down

**Earth NED**: N — North, E — East, D — Down

---

## Data Flow

```
ArduPilot SITL                     blimp_sim.py
     |                                 |
     |--- UDP servo packet (40B) ----->|
     |                                 | pwm_to_motors()
     |                                 | physics.step_rk4()
     |                                 | build_json_response()
     |<---- UDP JSON ------------------|
     |                                 |
     |       (repeats at ~250 Hz)      |
```
