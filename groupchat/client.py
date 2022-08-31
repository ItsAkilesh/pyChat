import threading
import socket
import threading

tag = input("Enter your tag: ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',12345))

def receiver():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'tag':
                client.send(tag.encode())
            else:
                print(message)
        except:
            client.close()
            break

def sender():
    while True:
        text = input()
        message = f"{tag}: {text}"
        client.send(message.encode())

listenThread = threading.Thread(target = receiver)
listenThread.start()

senderThread = threading.Thread(target = sender)
senderThread.start()