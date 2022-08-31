import socket

c = socket.socket()
c.connect(('localhost',12345))

try:
    while True:
        reply = c.recv(1024).decode()
        print("Jim: ",reply)
        msg = input("You: ")
        c.send(msg.encode())
except KeyboardInterrupt:
    exit("Your chat with Jim ended.")
