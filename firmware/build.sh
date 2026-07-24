#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# --- Defaults ---
VERBOSE=false
AUTO_SETUP=false
LOCAL=false

# --- Parse flags ---
while getopts "val" opt; do
    case $opt in
        v) VERBOSE=true ;;
        a) AUTO_SETUP=true ;;
        l) LOCAL=true ;;
        *) echo "Usage: $0 [-v] [-a] [-l]"; exit 1 ;;
    esac
done

source "$SCRIPT_DIR/config.env"

AP_DIR="$WORKSPACE/ardupilot"
VEHICLE_DIR="$WORKSPACE/ArduMotorBlimp"
OUTPUT_DIR="$SCRIPT_DIR/build"

ssh_cmd() {
    if [ "$LOCAL" = true ]; then
        eval "$@"
    else
        ssh "$VM_USER@$VM_HOST" "$@"
    fi
}

# --- Pre-flight checks ---
AP_OK=$(ssh_cmd "test -d '$AP_DIR/.git' && echo yes || echo no")
if [ "$AP_OK" != "yes" ]; then
    if [ "$AUTO_SETUP" = true ]; then
        echo "==> ArduPilot not found, running setup..."
        SETUP_ARGS=""
        [ "$LOCAL" = true ] && SETUP_ARGS="$SETUP_ARGS -l"
        [ "$VERBOSE" = true ] && SETUP_ARGS="$SETUP_ARGS -v"
        "$SCRIPT_DIR/setup.sh" $SETUP_ARGS
    else
        echo "ERROR: ArduPilot not found at $AP_DIR on VM"
        echo "Run ./setup.sh first (or use -a to auto-setup)"
        exit 1
    fi
fi

echo "============================================"
echo " ArduMotorBlimp Build"
[ "$LOCAL" = true ] && echo " Mode: local" || echo " VM: $VM_USER@$VM_HOST"
echo " Board: $BOARD"
[ "$VERBOSE" = true ] && echo " Output: verbose" || echo " Output: compact"
echo "============================================"
echo ""

# --- Update ArduMotorBlimp ---
echo "==> Updating ArduMotorBlimp ($VEHICLE_BRANCH)..."
ssh_cmd "cd '$VEHICLE_DIR' && git checkout $VEHICLE_BRANCH && git pull origin $VEHICLE_BRANCH"

# --- Copy to ArduPilot tree ---
echo "==> Copying to ArduPilot tree..."
ssh_cmd "cd '$AP_DIR' && rm -rf ArduMotorBlimp && cp -r '$VEHICLE_DIR' ./ArduMotorBlimp"

# --- Patch ArduPilot (idempotent) ---
echo "==> Patching ArduPilot build system..."
ssh_cmd "cd '$AP_DIR' && \
    grep -q 'ardumotorblimp' wscript || sed -i \"s/vehicles = \['antennatracker', 'blimp'/vehicles = ['antennatracker', 'ardumotorblimp', 'blimp'/\" wscript && \
    grep -q 'APM_BUILD_ArduMotorBlimp' libraries/AP_Vehicle/AP_Vehicle_Type.h || sed -i '/#define APM_BUILD_Blimp      12/a #define APM_BUILD_ArduMotorBlimp 13' libraries/AP_Vehicle/AP_Vehicle_Type.h"

# --- Build ---
echo "==> Building for $BOARD..."
if [ "$VERBOSE" = true ]; then
    ssh_cmd "cd '$AP_DIR' && rm -rf build/ && source '$WORKSPACE/venv/bin/activate' && ./waf configure --board $BOARD && ./waf build --target bin/ardublimp"
else
    ssh_cmd "cd '$AP_DIR' && rm -rf build/ && source '$WORKSPACE/venv/bin/activate' && ./waf configure --board $BOARD 2>&1 | tail -2 && ./waf build --target bin/ardublimp 2>&1 | tail -10"
fi

# --- Copy artifact locally ---
echo "==> Copying ardublimp.apj..."
mkdir -p "$OUTPUT_DIR"
if [ "$LOCAL" = true ]; then
    cp "$AP_DIR/build/$BOARD/bin/ardublimp.apj" "$OUTPUT_DIR/ardumotorblimp.apj"
else
    scp "$VM_USER@$VM_HOST:$AP_DIR/build/$BOARD/bin/ardublimp.apj" "$OUTPUT_DIR/ardumotorblimp.apj"
fi

echo ""
echo "==> Done!"
ls -lh "$OUTPUT_DIR/ardumotorblimp.apj"
