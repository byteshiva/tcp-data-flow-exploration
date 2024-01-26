# server.py

import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening for incoming connections...')

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()
    
    try:
        print('Connection from', client_address)
        
        # Send a welcome message to the client
        connection.sendall(b'Welcome to the server!')

    finally:
        # Clean up the connection
        connection.close()
