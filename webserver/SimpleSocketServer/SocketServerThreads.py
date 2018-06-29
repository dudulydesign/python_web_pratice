'''
Simple socket server using threads
https://www.binarytides.com/python-socket-server-code-example/

1. Create socket with socket.socket function
2. Bind socket to address+port with socket.bind function
3. Put the socket in listening mode with socket.listen function
3. Accept connection with socket.accept function
'''

import socket
import sys

HOST = ''   #symbolic name, meaning all available interfaces
PORT = 8888 #Arbitrary non-privileged port

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    socket.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code :' + str(msg[0]) + 'Message' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket'
socket.listen(10)
print 'Socket now listening'

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = socket.accept()
    print 'Connected with' + addr[0] + ':' + str(addr[1])
socket.close()
