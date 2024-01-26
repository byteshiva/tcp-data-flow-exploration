# client.py

import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Receive and print the welcome message from the server
    data = client_socket.recv(1024)
    print('Received:', data.decode())

    # Send a message to the server
    message = 'Hello, server!'
    client_socket.sendall(message.encode())

finally:
    # Clean up the connection
    client_socket.close()
