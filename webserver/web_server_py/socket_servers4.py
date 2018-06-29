'''
The simplest way to do this is to put the accept in a loop so that it can receive incoming connections all the time.
Live Server
So a live server will be alive always. Lets code this up
'''

import socket
import sys

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    server.bind((HOST, PORT))
except socket.error , msg:
  print 'Bind failed.Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
  sys.exit()

print 'Socket bind complete'

server.listen(10)
print 'Socket now listening'

#now keep talking with the client
while 1:
  #wait to accept a connection - blocking call
  conn, addr = server.accept()
  print 'Connected with ' + addr[0] + ':' + str(addr[1])

  data = conn.recv(1024)
  reply = 'OK...' + data
  if not data:
    break

  conn.sendall(reply)

conn.close()
server.close()
