import socket
import handler
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))


while True:
    data_from_server = s.recv(1024)
    print("Dwight : ", data_from_server.decode()) 