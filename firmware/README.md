# Firmware — ArduMotorBlimp for MicoAir H743 V2

Custom ArduMotorBlimp firmware built on ArduPilot Copter-4.6.3.

## Prerequisites

- SSH access to an Ubuntu VM (configured in `~/.ssh/config`) — for default (remote) mode
- VM with sudo privileges (for `setup.sh`)
- OR: local Ubuntu machine with build tools (for `-l` mode)

## Quick Start

```bash
# 1. Create your config.env from the template
cp config.env.example config.env
# edit VM_HOST, WORKSPACE to match your environment

# 2. Run setup (one time)
./setup.sh

# 3. Build the firmware
./build.sh
```

For local builds (no SSH):
```bash
cp config.env.example config.env
./setup.sh -l
./build.sh -l
```

## Flags

### `-v` / `--verbose`

Full output instead of compact (replaces old `-full` scripts).

```bash
./setup.sh -v          # verbose setup
./build.sh -v          # verbose build
```

### `-a` / `--auto-setup`

Build automatically runs `setup.sh` if ArduPilot is not found.

```bash
./build.sh -a          # auto-setup + build
./build.sh -a -v       # same, verbose
```

### `-l` / `--local`

All commands run locally instead of via SSH. When combined with `-a`, setup also runs locally.

```bash
./setup.sh -l          # local setup
./build.sh -l          # local build
./build.sh -a -l       # local build + local auto-setup
```

### `-h` / `--help`

Show help message.

```bash
./setup.sh --help
./build.sh --help
```

## Files

| File | Description |
|------|-------------|
| `config.env.example` | Config template (copy to `config.env`) |
| `config.env` | Your config (not committed) |
| `setup.sh` | First-run setup (`-v`, `-l`, `-h`) |
| `build.sh` | Build firmware (`-v`, `-a`, `-l`, `-h`) |
| `flash.md` | Flashing instructions via MicoAir Configurator |
| `build/` | Built `.apj` files |

## Configuration (config.env)

| Parameter | Description | Default |
|-----------|-------------|---------|
| `VM_HOST` | SSH host or alias | `my_vm` |
| `VM_USER` | SSH user | `your_user` |
| `WORKSPACE` | Workspace directory | `~/blimp_workspace` |
| `VEHICLE_BRANCH` | ArduMotorBlimp branch | `feat/manual-only` |
| `BOARD` | Target board | `MicoAir743v2` |

## What setup.sh does

1. Checks SSH access to VM (or runs locally with `-l`)
2. Checks/installs system dependencies (gcc-arm-none-eabi, python3, cmake)
3. Checks ArduPilot — clones Copter-4.6.3 if missing
4. Checks Python venv — creates with required packages if missing
5. Clones/updates ArduMotorBlimp
6. Patches ArduPilot build system (vehicles list + APM_BUILD macro)
7. Copies ArduMotorBlimp into ArduPilot tree

All steps are idempotent — re-running won't break existing setup.
