import socket
import handler

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 54321
s.connect((host, port))


while True:
    data_from_server = s.recv(1024)
    print("Jim: ", data_from_server)