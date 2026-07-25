# Blimp SITL — Docker Environment

Containerized ArduPilot SITL (Software In The Loop) simulation for the Blimp project.

## What's inside

- **Ubuntu 22.04** base image
- **ArduPilot Copter** (pinned stable release, compiled at build time)
- **MAVProxy** for ground station connectivity
- Pre-built SITL binary — container starts in seconds

## Quick start

### 1. Build the image

```bash
docker-compose build
```

> First build takes ~30 minutes (clones ArduPilot + compiles). Subsequent builds are fast.

### 2. Run

**Interactive shell** (manual control):
```bash
docker-compose up -d sitl
docker-compose exec sitl bash
sim_vehicle.py -v ArduMotorBlimp --console
```

**Auto-start** (boots straight into SITL with blimp params):
```bash
docker-compose up sitl-auto
```

### 3. Connect a GCS

Point QGroundControl / Mission Planner at:
- **UDP** `127.0.0.1:14550`
- **TCP** `127.0.0.1:5760`

## Project layout

```
sitl/
├── Dockerfile            # Image definition
├── docker-compose.yml    # Services: sitl, sitl-auto
├── README.md             # This file
├── .gitignore
├── params/               # ArduPilot parameters (mounted into container)
│   └── blimp.parm
└── scripts/              # Lua scripts (mounted into container)
    └── blimp_motors.lua
```

Edits to `params/` and `scripts/` on the host are picked up immediately — no rebuild needed.

## Useful commands

```bash
docker-compose ps          # list running containers
docker-compose logs -f     # follow logs
docker-compose exec sitl bash   # open shell inside container
docker-compose down -v     # stop and remove containers + volumes
```

## Rebuilding after Dockerfile changes

```bash
docker-compose build --no-cache
docker-compose up -d --force-recreate
```

## Troubleshooting

- **`sim_vehicle.py: command not found`** → run `export PATH=\$PATH:/home/blimp/ardupilot/Tools/autotest`
- **`python: not found`** → the Dockerfile creates a `python3` → `python` symlink; rebuild if missing
- **Time-went-backwards warnings** → harmless in WSL2; simulation still works
- **Port already in use** → stop other SITL instances or change `network_mode`

## License

See [LICENSE](../LICENSE) in the repository root.
