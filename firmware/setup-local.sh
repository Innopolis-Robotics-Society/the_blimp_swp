#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/config.env"

AP_DIR="$WORKSPACE/ardupilot"
VEHICLE_DIR="$WORKSPACE/ArduMotorBlimp"
VENV_DIR="$WORKSPACE/venv"
VEHICLE_REPO="https://github.com/DaniK-51/ArduMotorBlimp.git"
ARDUPILOT_BRANCH="Copter-4.6.3"

echo "============================================"
echo " ArduMotorBlimp Setup (local)"
echo " Workspace: $WORKSPACE"
echo " Board: $BOARD"
echo "============================================"
echo ""

# --- Step 1: Check/install system dependencies ---
echo "==> [1/4] Checking system dependencies..."
DEPS_OK=true
for cmd in git python3 arm-none-eabi-gcc cmake; do
    if ! command -v $cmd >/dev/null 2>&1; then
        echo "    Missing: $cmd"
        DEPS_OK=false
    fi
done

if [ "$DEPS_OK" = false ]; then
    echo "    Installing system dependencies (requires sudo)..."
    sudo apt update && sudo apt install -y git python3 python3-pip python3-venv gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential cmake ninja-build curl wget
    echo "    Dependencies installed"
else
    echo "    All dependencies present"
fi

# --- Step 2: Check ArduPilot ---
echo "==> [2/4] Checking ArduPilot..."
if [ -d "$AP_DIR/.git" ]; then
    AP_TAG=$(cd "$AP_DIR" && git describe --tags --exact-match 2>/dev/null || git log --oneline -1)
    echo "    ArduPilot found at $AP_DIR"
    echo "    Version: $AP_TAG"
    if echo "$AP_TAG" | grep -q "$ARDUPILOT_BRANCH"; then
        echo "    Branch matches $ARDUPILOT_BRANCH"
    else
        echo "    WARNING: Expected branch $ARDUPILOT_BRANCH, got $AP_TAG"
        echo "    ArduPilot will NOT be re-cloned automatically."
        echo "    If wrong version, delete $AP_DIR and re-run this script."
    fi
else
    echo "    Cloning ArduPilot $ARDUPILOT_BRANCH (this may take 5-15 minutes)..."
    mkdir -p "$WORKSPACE" && cd "$WORKSPACE" && git clone --branch $ARDUPILOT_BRANCH --recursive https://github.com/ArduPilot/ardupilot.git
    echo "    ArduPilot cloned"
fi

# --- Step 3: Python venv ---
echo "==> [3/4] Checking Python venv..."
if [ -d "$VENV_DIR" ]; then
    echo "    venv already exists at $VENV_DIR"
else
    echo "    Creating Python venv..."
    mkdir -p "$WORKSPACE" && cd "$WORKSPACE" && python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip wheel setuptools && pip install 'setuptools<70.0.0' 'empy==3.3.4' future toml numpy packaging jinja2 pexpect dronecan
    echo "    venv created with dependencies"
fi

# --- Step 4: ArduMotorBlimp ---
echo "==> [4/4] Checking ArduMotorBlimp..."
if [ -d "$VEHICLE_DIR/.git" ]; then
    cd "$VEHICLE_DIR" && git fetch origin && git checkout $VEHICLE_BRANCH && git pull origin $VEHICLE_BRANCH
    echo "    ArduMotorBlimp updated to $VEHICLE_BRANCH"
else
    mkdir -p "$WORKSPACE" && cd "$WORKSPACE" && git clone --branch $VEHICLE_BRANCH $VEHICLE_REPO
    echo "    ArduMotorBlimp cloned"
fi

# --- Patch ArduPilot ---
echo "==> Patching ArduPilot build system..."
cd "$AP_DIR" && \
    grep -q 'ardumotorblimp' wscript || sed -i "s/vehicles = \['antennatracker', 'blimp'/vehicles = ['antennatracker', 'ardumotorblimp', 'blimp'/" wscript && \
    grep -q 'APM_BUILD_ArduMotorBlimp' libraries/AP_Vehicle/AP_Vehicle_Type.h || sed -i '/#define APM_BUILD_Blimp      12/a #define APM_BUILD_ArduMotorBlimp 13' libraries/AP_Vehicle/AP_Vehicle_Type.h

# --- Copy vehicle into ArduPilot tree ---
echo "==> Copying ArduMotorBlimp into ArduPilot tree..."
cd "$AP_DIR" && rm -rf ArduMotorBlimp && cp -r "$VEHICLE_DIR" ./ArduMotorBlimp

echo ""
echo "============================================"
echo " Setup complete!"
echo " Next: ./build-local-full.sh (or ./build-local.sh)"
echo "============================================"
