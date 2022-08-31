import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',12345))
server.listen()
conn,add = server.accept()

try:
    while True:
        msg = input("You: ")
        conn.send((msg).encode())
        reply = conn.recv(1024).decode()
        print("Dwight: ",reply)
except KeyboardInterrupt:
    exit("Your chat with Dwight ended.")