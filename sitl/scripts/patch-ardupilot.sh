#!/bin/bash
set -euo pipefail

ARDUPILOT_DIR="$1"

# 1. Register ArduMotorBlimp in waf vehicles list
sed -i "s/vehicles = \['antennatracker', 'blimp'/vehicles = ['antennatracker', 'ardumotorblimp', 'blimp'/" \
    "$ARDUPILOT_DIR/wscript"

# 2. Define APM_BUILD_ArduMotorBlimp in AP_Vehicle_Type.h
sed -i 's/#define APM_BUILD_Heli       13/#define APM_BUILD_Heli       13\n#define APM_BUILD_ArduMotorBlimp 14/' \
    "$ARDUPILOT_DIR/libraries/AP_Vehicle/AP_Vehicle_Type.h"

# 3. Register ArduMotorBlimp in vehicleinfo.py (sim_vehicle.py frame lookup)
python3 -c "
path = '$ARDUPILOT_DIR/Tools/autotest/pysim/vehicleinfo.py'
with open(path) as f:
    c = f.read()
entry = '''
    \"ArduMotorBlimp\": {
        \"default_frame\": \"ArduMotorBlimp\",
        \"frames\": {
            \"ArduMotorBlimp\": {
                \"waf_target\": \"bin/ardublimp\",
                \"default_params_filename\": \"default_params/blimp.parm\",
            },
        },
    },
'''
c = c.replace('    \"Blimp\": {', '    \"Blimp\": {' + entry, 1)
with open(path, 'w') as f:
    f.write(c)
"

# 4. Register ArduMotorBlimp in sim_vehicle.py vehicle_map
sed -i 's/"Blimp" : "Blimp",/"ArduMotorBlimp" : "ArduMotorBlimp",\n    "Blimp" : "Blimp",/' \
    "$ARDUPILOT_DIR/Tools/autotest/sim_vehicle.py"

echo "ArduMotorBlimp registered in ArduPilot build system."
