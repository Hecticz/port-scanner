#!/bin/python 

#python3 scanner.py ip 

import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])  #Translate hostname to ipv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>") 
	

#scan
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now() ))
print("-" * 50)

try:
#port range can be changed 1,6000
	for port in range(22,85):
	         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	         socket.setdefaulttimeout(1)
	         result = s.connect_ex((target,port))  #returns an error indicator
#	         print("Checking port {} is open" .format(port))
	if result == 0:
		print("Port {} is open".format(port))
	s.close()
	
except KeyboardInterrupt:
	print("\nExiting program. ")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to server.")	
	sys.exit()				
	

