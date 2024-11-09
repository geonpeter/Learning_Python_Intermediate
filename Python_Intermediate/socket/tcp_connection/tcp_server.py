import socket

# 1. Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind the server to an IP address and port
server_socket.bind(("localhost", 12345))

# 3. Start listening for connections
server_socket.listen(1)
print("Server is listening on port 12345...")

# 4. Accept a connection from a client
connection, address = server_socket.accept()
print("Connected to client at:", address)

# 5. Chat loop: keep sending and receiving messages
while True:
    # Receive a message from the client
    client_message = connection.recv(1024).decode()
    print("Client says:", client_message)
    
    # Break the loop if the client says "bye"
    if client_message.lower() == "bye":
        print("Ending chat.")
        break
    
    # Send a message back to the client
    server_message = input("Server: ")
    connection.sendall(server_message.encode())

# 6. Close the connection
connection.close()
server_socket.close()
