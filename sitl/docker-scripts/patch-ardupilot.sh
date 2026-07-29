#!/bin/bash
set -euo pipefail

ARDUPILOT_DIR="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 1. Register 'motorblimp' in waf vehicles list
sed -i "s/vehicles = \['antennatracker', 'blimp', 'copter', 'heli', 'plane', 'rover', 'sub'\]/vehicles = ['antennatracker', 'blimp', 'copter', 'heli', 'motorblimp', 'plane', 'rover', 'sub']/" \
    "$ARDUPILOT_DIR/wscript"

# 2. Define APM_BUILD_ArduMotorBlimp in AP_Vehicle_Type.h
sed -i '/#define APM_BUILD_Heli       13/a #define APM_BUILD_ArduMotorBlimp  14' \
    "$ARDUPILOT_DIR/libraries/AP_Vehicle/AP_Vehicle_Type.h"

# 3. Add streamrates for ArduMotorBlimp in GCS_MAVLink_Parameters.cpp
GCS_PARAMS="$ARDUPILOT_DIR/libraries/GCS_MAVLink/GCS_MAVLink_Parameters.cpp"
if ! grep -q "APM_BUILD_ArduMotorBlimp" "$GCS_PARAMS"; then
    sed -i '/^#elif APM_BUILD_COPTER_OR_HELI/i \
#elif APM_BUILD_TYPE(APM_BUILD_ArduMotorBlimp)\
#define AP_MAV_DEFAULT_STREAM_RATE_RAW_SENS 0\
#define AP_MAV_DEFAULT_STREAM_RATE_EXT_STAT 1\
#define AP_MAV_DEFAULT_STREAM_RATE_RC_CHAN 10\
#define AP_MAV_DEFAULT_STREAM_RATE_RAW_CTRL 0\
#define AP_MAV_DEFAULT_STREAM_RATE_POSITION 0\
#define AP_MAV_DEFAULT_STREAM_RATE_EXTRA1 10\
#define AP_MAV_DEFAULT_STREAM_RATE_EXTRA2 0\
#define AP_MAV_DEFAULT_STREAM_RATE_EXTRA3 0\
#define AP_MAV_DEFAULT_STREAM_RATE_PARAMS 0\
#define AP_MAV_DEFAULT_STREAM_RATE_ADSB 0' "$GCS_PARAMS"
fi

# 4. Register ArduMotorBlimp in vehicleinfo.py (sim_vehicle.py frame lookup)
python3 "$SCRIPT_DIR/patch_vehicleinfo.py" "$ARDUPILOT_DIR"

# 5. Register ArduMotorBlimp in sim_vehicle.py vehicle_map
sed -i 's/"Blimp" : "Blimp",/"ArduMotorBlimp" : "ArduMotorBlimp",\n    "Blimp" : "Blimp",/' \
    "$ARDUPILOT_DIR/Tools/autotest/sim_vehicle.py"

echo "ArduMotorBlimp registered in ArduPilot build system."
