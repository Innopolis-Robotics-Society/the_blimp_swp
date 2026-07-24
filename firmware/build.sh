#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/config.env"

AP_DIR="$WORKSPACE/ardupilot"
VEHICLE_DIR="$WORKSPACE/ArduMotorBlimp"
OUTPUT_DIR="$SCRIPT_DIR/build"

# --- Pre-flight checks ---
AP_OK=$(ssh "$VM_USER@$VM_HOST" "test -d '$AP_DIR/.git' && echo yes || echo no")
if [ "$AP_OK" != "yes" ]; then
    echo "ERROR: ArduPilot not found at $AP_DIR on VM"
    echo "Run ./setup.sh first"
    exit 1
fi

# --- Update ArduMotorBlimp ---
echo "==> Updating ArduMotorBlimp ($VEHICLE_BRANCH)..."
ssh "$VM_USER@$VM_HOST" "cd '$VEHICLE_DIR' && git checkout $VEHICLE_BRANCH && git pull origin $VEHICLE_BRANCH"

# --- Copy to ArduPilot tree ---
echo "==> Copying to ArduPilot tree..."
ssh "$VM_USER@$VM_HOST" "cd '$AP_DIR' && rm -rf ArduMotorBlimp && cp -r '$VEHICLE_DIR' ./ArduMotorBlimp"

# --- Patch ArduPilot (idempotent) ---
echo "==> Patching ArduPilot build system..."
ssh "$VM_USER@$VM_HOST" "cd '$AP_DIR' && \
    grep -q 'ardumotorblimp' wscript || sed -i \"s/vehicles = \['antennatracker', 'blimp'/vehicles = ['antennatracker', 'ardumotorblimp', 'blimp'/\" wscript && \
    grep -q 'APM_BUILD_ArduMotorBlimp' libraries/AP_Vehicle/AP_Vehicle_Type.h || sed -i '/#define APM_BUILD_Blimp      12/a #define APM_BUILD_ArduMotorBlimp 13' libraries/AP_Vehicle/AP_Vehicle_Type.h"

# --- Build ---
echo "==> Building for $BOARD..."
ssh "$VM_USER@$VM_HOST" "cd '$AP_DIR' && rm -rf build/ && source '$WORKSPACE/venv/bin/activate' && ./waf configure --board $BOARD 2>&1 | tail -2 && ./waf build --target bin/ardublimp 2>&1 | tail -10"

# --- Copy artifact locally ---
echo "==> Copying ardublimp.apj to local..."
mkdir -p "$OUTPUT_DIR"
scp "$VM_USER@$VM_HOST:$AP_DIR/build/$BOARD/bin/ardublimp.apj" "$OUTPUT_DIR/ardumotorblimp.apj"

echo ""
echo "==> Done!"
ls -lh "$OUTPUT_DIR/ardumotorblimp.apj"
