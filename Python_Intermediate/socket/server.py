import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',55555))
s.listen()
print('Listening...')
while True:
    client,address = s.accept()
    print("Connected to {}".format(address))
    client.send("Client, You are connected ".encode('utf-8'))
    client.close()