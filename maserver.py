#!/usr/bin/env python3

import sys
import telnetlib
import time
import socket

# IP and port — grandma default port for control is 30000 and username/password
if len(sys.argv) > 1:
    TelHOST = sys.argv[1]
else:
    print("""Usage:
    python3 script.py <ip> <port> <username> <password>
    Example: python3 script.py 192.168.0.10 30000 admin 1234

    Maclient is used to send from command line or linux show player to this program
    """)
    sys.exit()

TelPORT = int(sys.argv[2])
MaUser = sys.argv[3]
MaPass = sys.argv[4]

# Login to MA2
try:
    tn = telnetlib.Telnet(TelHOST, TelPORT)
except Exception as e:
    print(f"Connection failed: {e}")
    sys.exit(1)

time.sleep(5)
login_cmd = f'Login "{MaUser}" "{MaPass}"\r'
tn.write(login_cmd.encode('ascii'))
time.sleep(2)
print("Login into Grandma2 — check on lightdesk if successful.")


def server_program():
    # Default localhost:5050
    host = "localhost"
    port = 5050

    server_socket = socket.socket()
    server_socket.bind((host, port))

    while True:
        server_socket.listen(2)
        conn, address = server_socket.accept()
        print(f"Connection from: {address}")

        data = conn.recv(2560).decode().strip()
        if not data:
            print("No command received — check input.")
            conn.close()
            continue

        print(f"From connected user: {data}")
        tn.write((data + "\r").encode('ascii'))  # send command to telnet session
        print("Sent to telnet.")
        conn.close()


# Call main loop
if __name__ == '__main__':
    server_program()
