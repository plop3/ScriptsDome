#!/usr/bin/python3
#
# Status script for INDI Dome Scripting Gateway
#
# Arguments: file name to save current state and coordinates (parked ra dec)
# Exit code: 0 for success, 1 for failure
#

import sys
import requests

script, path = sys.argv

status = open(path, 'w')
status.truncate()
try:
    r = requests.get("http://192.168.0.17/state")
    status.write(r.content.decode("utf-8"))
except:
    coordinates = open('/tmp/indi-status', 'r')
    status.write(coordinates.readline())
status.close()
sys.exit(0)

