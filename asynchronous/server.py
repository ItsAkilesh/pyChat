import lib

if __name__ == '__main__':
    sender = lib.senderThread("You", 8080)
    sender.start()
   
    receiver= lib.recvThread("Jim", 8081)
    receiver.start()
   
    sender.join()
    receiver.join() 
