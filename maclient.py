#!/usr/bin/env python3
"""
Send a command to maserver.py from Linux Show Player or command line.
This script connects to the local socket (default localhost:5050)
and sends a command string.
"""

import socket
import sys

def main():
    host = "localhost"
    port = 5050

    if len(sys.argv) < 2:
        print("Usage: python3 send_to_ma.py \"<command>\"")
        sys.exit(1)

    message = sys.argv[1]
    print(f"Sending: {message}")  # Debug message

    try:
        # Create socket and connect
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            client_socket.connect((host, port))
            client_socket.sendall(message.encode('utf-8'))  # send command
            print("Command sent successfully.")
    except ConnectionRefusedError:
        print(f"Error: Could not connect to {host}:{port}. Is maserver.py running?")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
