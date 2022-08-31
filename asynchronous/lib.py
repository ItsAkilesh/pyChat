import socket
import threading

class senderThread(threading.Thread):
    def __init__(self, name, port ):
        threading.Thread.__init__(self)
        self.name = name
        self.port = port 
        self.s = self._create_socket()

    def run(self):
        while True:
            try:
                sendData=input(f"{self.name}: ")
                self.s.send(bytes(sendData,'utf-8'))
            except KeyboardInterrupt:
                self._close_socket()
    def _close_socket(self):
        self.conn.close()
    def _create_socket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'Waiting for Receiver to connnect to {self.port} ')
        self.s.connect(('localhost', self.port))
        return self.s
   

class recvThread(threading.Thread):
    def __init__(self, name, port ):
        threading.Thread.__init__(self)
        self.name = name
        self.port = port 
        self.conn = self._create_socket()

    def run(self):
        while True:
            try:
                recvData = self.conn.recv(1024).decode()
                if recvData == '':
                    break
                print(f'{self.name}: ',recvData)
            except KeyboardInterrupt:
                self._close_socket()
    def _close_socket(self):
        self.conn.close()
    def _create_socket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('',self.port))
        self.s.listen()
        print(f'Waiting for Senders to connnect to {self.port}')
        conn , addr = self.s.accept()
        print(f'Connected to {addr}!')
        return conn

