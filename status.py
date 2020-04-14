#!/usr/bin/python3
#
# Status script for INDI Dome Scripting Gateway
#
# Arguments: file name to save current state and coordinates (parked ra dec)
# Exit code: 0 for success, 1 for failure
#

import sys
import socket
import time

IP="dome"
PORT=23

# Lecture de l'etat du dome et mise a jour du pilote Indi

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP,PORT))
s.send(b"P?#")
rep=s.recv(1024).decode()[0]
if rep=='1':
    retP='1'
else:
    retP='0'
s.close()
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((IP,PORT))
s2.send(b"D?#")
rep=s2.recv(1024).decode()[0]
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
