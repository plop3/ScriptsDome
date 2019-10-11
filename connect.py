#!/usr/bin/python3
#
# Connect script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

import sys
import socket

IP="localhost"
PORT=1234

# Lecture de l'etat du dome et mise a jour du pilote Indi

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP,PORT))
s.send(b"P?#")
rep=s.recv(1024).decode()[0]
if rep=='1':
    retP='1'
else:
    retP='0'
s.send(b"D?#")
rep=s.recv(1024).decode()[0]
if rep=='1':
    retD='0'
else:
    retD='1'

s.close()

coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
coordinates.write(retD+' '+retP+' 0')
coordinates.close()

sys.exit(0)
