#!/usr/bin/env python3
"""Register ArduMotorBlimp in ArduPilot's vehicleinfo.py."""
import sys

ARDUPILOT_DIR = sys.argv[1]
path = f"{ARDUPILOT_DIR}/Tools/autotest/pysim/vehicleinfo.py"

with open(path) as f:
    c = f.read()

old = '''    },
    "ArduPlane": {'''

new = '''    },
    "ArduMotorBlimp": {
        "default_frame": "ArduMotorBlimp",
        "frames": {
            "ArduMotorBlimp": {
                "model": "Blimp",
                "waf_target": "bin/ardumotorblimp",
                "default_params_filename": "default_params/blimp.parm",
            },
        },
    },
    "ArduPlane": {'''

if old not in c:
    print("ERROR: pattern not found in vehicleinfo.py", file=sys.stderr)
    sys.exit(1)

c = c.replace(old, new, 1)

with open(path, "w") as f:
    f.write(c)

print("ArduMotorBlimp added to vehicleinfo.py")
