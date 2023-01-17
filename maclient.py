#!/usr/bin/env python2

#send command to telenet from linux show player
#This script will send the commands to Telnetsend.py witch has a telnet connenctoin to ma running in the background

import socket
import sys
import time

#Default localhost 5050
host = "localhost"  
port = 5050  

client_socket = socket.socket()  
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client_socket.connect((host, port))  # connect to the server

message = sys.argv[1]  # take input Because of spaces use ""

print(message) #Debug use wil not be seen in show player

client_socket.send(message.encode())  # send message
  # show in terminal Debug use

client_socket.close()  # close the connection