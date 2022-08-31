import lib
# client=socket.socket()
# client.connect(("localhost",12346))
if __name__ == '__main__':
    receiver= lib.recvThread("Dwight", 8080)
    receiver.start()
    
    sender = lib.senderThread("You", 8081)
    sender.start()
    sender.join()
    receiver.join() 

