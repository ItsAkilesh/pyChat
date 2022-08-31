import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
print("Connection From: ", addr)

while True:
    inp = input("You: ")
    conn.sendall(inp.encode())