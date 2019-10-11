#!/usr/bin/python3
#
# Open shutter script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

import sys
import  socket

IP="dome"
PORT=1234
status=0
# Ouverture des portes
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP,PORT))
s.send(b"P+#")
rep=s.recv(1024).decode()[0]
if (rep=="1"):
    ret=" 1 "
else:
    ret=" 0 "
    #ret=" 1 "
    status=1
    #status=0

s.close()

coordinates = open('/tmp/indi-status', 'r')
str = coordinates.readline()
coordinates.close()
str = str[0] + ret + str[4:]
coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
coordinates.write(str)
coordinates.close()

sys.exit(status)
