# Interface Specification

## Type
MAVLink + CLI

## Intended users
Developers and test engineers who run simulations.

## MAVLink messages
- `MAV_CMD_NAV_WAYPOINT` – send waypoint
- `MAV_CMD_DO_SET_MODE` – change flight mode
- `HEARTBEAT` – check connection
- `GLOBAL_POSITION_INT` – get telemetry

## CLI commands
python3 backend.py --mission mission.txt
python3 backend.py --status
python3 backend.py --arm

## Example (success)
$ python3 backend.py --mission waypoints.txt
Heartbeat received. Mission uploaded. Telemetry OK.

## Example (error)
$ python3 backend.py --mission missing.txt
Error: File not found.

## Smoke-check
1. Start SITL
2. Run python3 backend.py
3. Check: heartbeat received, telemetry updates
