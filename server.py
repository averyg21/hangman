####################Imports##########################
from random import randint
import atexit
import sys
import socket
####################Imports##########################

#create an INET, Streaming socket
def prog1():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind(host,port)

    #listen to one connection at a time.
    s.listen(1)
    #return new connection and address
    c, addr = s.accept()
    print("Connection from: ", str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("From connected user: " + str(data))
        data = str(data)