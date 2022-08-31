import socket 
import threading

host = 'localhost'
port = 12345

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((host,port))
server.listen(100)

clients = []
tags = []

def broadcast(message):
	for client in clients:
		client.send(message)

def clientControl(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			pos = clients.index(client)
			clients.remove(pos)
			client.close()
			tag = tags[pos]
			broadcast(f"{tag} left the room.")
			tags.remove(tag)
			break

def receiver():
    while True: 
        client,addr = server.accept()
        print(f"{addr} connected.")
        client.send('tag'.encode())
        tag = client.recv(1024).decode()
        tags.append(tag)
        clients.append(client)

        broadcast(f"{tag} joined.".encode())
        client.send('Connected to server.'.encode())

        thread = threading.Thread(target=clientControl, args=(client,))
        thread.start()
receiver()