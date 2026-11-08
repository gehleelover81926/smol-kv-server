import socket

PORT=6380
HOST="127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(b"SET username jynjo\n")
print(client.recv(1024).decode())

client.sendall(b"GET username\n")
print(client.recv(1024).decode('utf-8'))

client.sendall(b"DEL username\n")
print(client.recv(1024).decode('utf-8'))

client.sendall(b"PING\n")
print(client.recv(1024).decode('utf-8'))
