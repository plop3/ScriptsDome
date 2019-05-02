#!/usr/bin/python
#
# Abort script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

import sys
import serial
import time

DOME='/dev/Dome'

ser=serial.Serial(DOME)
time.sleep(2)
ser.write(b'AU')

sys.exit(0)

