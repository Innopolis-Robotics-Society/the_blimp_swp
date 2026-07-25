#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# --- Defaults ---
VERBOSE=false
AUTO_SETUP=false
LOCAL=false
HEX_ONLY=false

# --- Parse flags ---
print_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Build ArduMotorBlimp firmware for MicoAir H743 V2."
    echo ""
    echo "Options:"
    echo "  -v, --verbose       Verbose output (full waf output)"
    echo "  -a, --auto-setup    Auto-run setup.sh if ArduPilot not found"
    echo "  -l, --local         Run commands locally instead of via SSH"
    echo "  --hex               Generate DFU hex from existing .bin (skip build)"
    echo "  -h, --help          Show this help message"
}

while [ $# -gt 0 ]; do
    case "$1" in
        -v|--verbose) VERBOSE=true; shift ;;
        -a|--auto-setup) AUTO_SETUP=true; shift ;;
        -l|--local) LOCAL=true; shift ;;
        --hex) HEX_ONLY=true; shift ;;
        -h|--help) print_usage; exit 0 ;;
        *) echo "Unknown option: $1"; print_usage; exit 1 ;;
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
        echo "ERROR: ArduPilot not found at $AP_DIR"
        echo "Run ./setup.sh first (or use -a / --auto-setup)"
        exit 1
    fi
fi

echo "============================================"
echo " ArduMotorBlimp Build"
[ "$LOCAL" = true ] && echo " Mode: local" || echo " VM: $VM_USER@$VM_HOST"
echo " Board: $BOARD"
if [ "$HEX_ONLY" = true ]; then
    echo " Mode: hex only (skip build)"
elif [ "$LOCAL" = true ]; then
    echo " Mode: local"
else
    echo " VM: $VM_USER@$VM_HOST"
fi
[ "$VERBOSE" = true ] && echo " Output: verbose" || echo " Output: compact"
echo "============================================"
echo ""

if [ "$HEX_ONLY" = false ]; then
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
fi

# --- Generate hex for DFU flashing ---
echo "==> Generating DFU hex file..."
ssh_cmd "cd '$AP_DIR' && source '$WORKSPACE/venv/bin/activate' && pip install intelhex -q && python Tools/scripts/make_intel_hex.py build/$BOARD/bin/ardublimp.bin Tools/bootloaders/${BOARD}_bl.bin 128"

# --- Copy artifacts locally ---
echo "==> Copying artifacts..."
mkdir -p "$OUTPUT_DIR"
if [ "$LOCAL" = true ]; then
    cp "$AP_DIR/build/$BOARD/bin/ardublimp.apj" "$OUTPUT_DIR/ardumotorblimp.apj"
    cp "$AP_DIR/build/$BOARD/bin/ardublimp_with_bl.hex" "$OUTPUT_DIR/ardumotorblimp_with_bl.hex"
else
    scp "$VM_USER@$VM_HOST:$AP_DIR/build/$BOARD/bin/ardublimp.apj" "$OUTPUT_DIR/ardumotorblimp.apj"
    scp "$VM_USER@$VM_HOST:$AP_DIR/build/$BOARD/bin/ardublimp_with_bl.hex" "$OUTPUT_DIR/ardumotorblimp_with_bl.hex"
fi

echo ""
echo "==> Done!"
ls -lh "$OUTPUT_DIR/"
