#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/config.env"

AP_DIR="$WORKSPACE/ardupilot"
VEHICLE_DIR="$WORKSPACE/ArduMotorBlimp"
OUTPUT_DIR="$SCRIPT_DIR/build"

# --- Pre-flight checks ---
if [ ! -d "$AP_DIR/.git" ]; then
    echo "ERROR: ArduPilot not found at $AP_DIR"
    echo "Run ./setup-local.sh first"
    exit 1
fi

# --- Update ArduMotorBlimp ---
echo "==> Updating ArduMotorBlimp ($VEHICLE_BRANCH)..."
cd "$VEHICLE_DIR" && git checkout $VEHICLE_BRANCH && git pull origin $VEHICLE_BRANCH

# --- Copy to ArduPilot tree ---
echo "==> Copying to ArduPilot tree..."
cd "$AP_DIR" && rm -rf ArduMotorBlimp && cp -r "$VEHICLE_DIR" ./ArduMotorBlimp

# --- Patch ArduPilot (idempotent) ---
echo "==> Patching ArduPilot build system..."
cd "$AP_DIR" && \
    grep -q 'ardumotorblimp' wscript || sed -i "s/vehicles = \['antennatracker', 'blimp'/vehicles = ['antennatracker', 'ardumotorblimp', 'blimp'/" wscript && \
    grep -q 'APM_BUILD_ArduMotorBlimp' libraries/AP_Vehicle/AP_Vehicle_Type.h || sed -i '/#define APM_BUILD_Blimp      12/a #define APM_BUILD_ArduMotorBlimp 13' libraries/AP_Vehicle/AP_Vehicle_Type.h

# --- Build ---
echo "==> Building for $BOARD..."
cd "$AP_DIR" && rm -rf build/ && source "$WORKSPACE/venv/bin/activate" && ./waf configure --board $BOARD 2>&1 | tail -2 && ./waf build --target bin/ardublimp 2>&1 | tail -10

# --- Copy artifact locally ---
echo "==> Copying ardublimp.apj..."
mkdir -p "$OUTPUT_DIR"
cp "$AP_DIR/build/$BOARD/bin/ardublimp.apj" "$OUTPUT_DIR/ardumotorblimp.apj"

echo ""
echo "==> Done!"
ls -lh "$OUTPUT_DIR/ardumotorblimp.apj"
