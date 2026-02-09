#!/usr/bin/env python3
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  

# Create, bind, and listen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print(f"Listening on {TCP_IP}:{TCP_PORT}...")

    conn, addr = s.accept()
    with conn:
        print("Connection address:", addr)
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            print("Received data:", data.decode(errors='ignore'))
            conn.sendall(data)  # Echo back to client
        print("Connection closed.")
