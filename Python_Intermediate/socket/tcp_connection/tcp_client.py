import socket

# 1. Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server at the specified address and port
client_socket.connect(("localhost", 12345))
print("Connected to the server!")

# 3. Chat loop: keep sending and receiving messages
while True:
    # Send a message to the server
    client_message = input("Client: ")
    client_socket.sendall(client_message.encode())
    
    # Break the loop if the client says "bye"
    if client_message.lower() == "bye":
        print("Ending chat.")
        break
    
    # Receive a message from the server
    server_message = client_socket.recv(1024).decode()
    print("Server says:", server_message)

# 4. Close the connection
client_socket.close()
