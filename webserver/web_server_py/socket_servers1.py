'''
OK now onto server things. Servers basically do the following :

1. Open a socket
2. Bind to a address(and port).
3. Listen for incoming connections.
4. Accept connections
5. Read/Send

We have already learnt how to open a socket. So the next thing would be to bind it.

Bind a socket
Function bind can be used to bind a socket to a particular address and port. It needs a sockaddr_in structure similar to connect function.

Quick example
'''

import socket
import sys

HOST = ''   #Symbolic name meaning all available interfaces
PORT = 8888 #Arbitrary non-privileged port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    server.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

'''
Listen for incoming connections
After binding a socket to a port the next thing we need to do is listen for connections. 
For this we need to put the socket in listening mode. 
Function socket_listen is used to put the socket in listening mode. Just add the following line after bind.
'''

server.listen(10)
print 'Socket now listening'



