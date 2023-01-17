#!/usr/bin/env python2


import sys
import telnetlib
import time
import socket

# IP and port grandma default port for control is 30000 and usernam and password
if len(sys.argv) > 1:
    TelHOST = (sys.argv[1])
else:
    TelHOST = "help"
    print("""To use this program first argv  is ip address of the lightdesk
argv 2 is the port (Default 3000 to control)
argv 3 is your user name
argv 4 is your password
Maclient is used to send from command line or linux show player to this program""")
    exit()    
TelPORT = (sys.argv[2])
MaUser = (sys.argv[3])
MaPass = (sys.argv[4])

#login to ma Default port for control is 30000
#This need to be checked for delays. If they are needed

tn = telnetlib.Telnet(TelHOST, TelPORT)
time.sleep(5)
tn.write('Login' +  ' "' + MaUser + '" ' + '"' + MaPass + '"' +"\r")
time.sleep(2)
print("Login into Grandma2 check on lightdesk if succesful")


def server_program():
	#Default localhost 5050
    host = "localhost"
    port = 5050  

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    
    while True:
    	server_socket.listen(2) 
    	conn, address = server_socket.accept() # accept new connection
    	print("Connection from: " + str(address))
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(2560).decode()
        if not data:
            # if data no data close and continu
            print("No command recviede check input")
            conn.close() 
            continue
        print("from connected user: " + str(data))
        tn.write((str(data)) + "\r") #send command to telnet session and press enter
        print("Send to telnet")
      # send data to the client
        conn.close()  # close the connection

    

#Call main loop
if __name__ == '__main__':
    server_program()

