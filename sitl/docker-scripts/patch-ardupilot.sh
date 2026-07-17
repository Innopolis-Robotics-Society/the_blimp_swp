#!/bin/bash
set -euo pipefail

ARDUPILOT_DIR="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 1. Register ArduMotorBlimp in waf vehicles list
sed -i "s/vehicles = \['antennatracker', 'blimp'/vehicles = ['antennatracker', 'ardumotorblimp', 'blimp'/" \
    "$ARDUPILOT_DIR/wscript"

# 2. Define APM_BUILD_ArduMotorBlimp in AP_Vehicle_Type.h
sed -i 's/#define APM_BUILD_Heli       13/#define APM_BUILD_Heli       13\n#define APM_BUILD_ArduMotorBlimp 14/' \
    "$ARDUPILOT_DIR/libraries/AP_Vehicle/AP_Vehicle_Type.h"

# 3. Register ArduMotorBlimp in vehicleinfo.py (sim_vehicle.py frame lookup)
python3 "$SCRIPT_DIR/patch_vehicleinfo.py" "$ARDUPILOT_DIR"

# 4. Register ArduMotorBlimp in sim_vehicle.py vehicle_map
sed -i 's/"Blimp" : "Blimp",/"ArduMotorBlimp" : "ArduMotorBlimp",\n    "Blimp" : "Blimp",/' \
    "$ARDUPILOT_DIR/Tools/autotest/sim_vehicle.py"

echo "ArduMotorBlimp registered in ArduPilot build system."
