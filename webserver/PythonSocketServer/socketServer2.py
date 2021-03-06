﻿
import socket
import sys
from thread import *

#======================================
HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
#======================================
#bind socket to local host and port 
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code:' + str(msg[0]) + 'Message' + msg[1]
    sys.exit()
print 'Socket bind complete'

#======================================

#監聽連接
s.listen(10)
print 'Socket now listening'

#======================================

#Function for handling connections.This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the ser ver . Type something and hit enter\n')
    #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:
      #receiving from client
      data = conn.recv(1024)
      reply = 'OK...' + data
      if not data:
          break
      conn.sendall(reply)

    #came out of loop
    conn.close()

#now keep talking with the client
while 1:

    #接收連接
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    #======================================

    #display client information
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #======================================

    #start new thread takes 1st argument as a function name to be run, second is th tuple of arguments to the function.
    start_new_thread(clientthread , (conn,))


s.close()


