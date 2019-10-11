#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Park script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

# Script de gestion de l'abri
# Ouverture de l'abri

import os
import sys
import socket

IP="dome"
PORT=1234

status=0

# Fermeture de l'abri
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP,PORT))
s.send(b"D-#")
rep=s.recv(1024).decode()[0]
if (rep=="1"):
    ret="1"
else:
    ret="0"
    status=1

#os.system("/usr/local/bin/park.py &")

coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
coordinates.write(ret+' 0 0')
#coordinates.write('1 0 0')
coordinates.close()

sys.exit(status)
