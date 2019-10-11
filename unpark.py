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

# Ouverture de l'abri
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP,PORT))
s.send(b"D+#")
rep=s.recv(1024).decode()[0]
if (rep=="1"):
    ret="0"
else:
    ret="1"
    status=1

s.close()

coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
#coordinates.write('0 0 0')
coordinates.write(ret+' 1 0')
coordinates.close()

sys.exit(0)

