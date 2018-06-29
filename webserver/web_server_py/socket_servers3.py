'''
So we can see that the client connected to the server. Try the above steps till you get it working perfect.

We accepted an incoming connection but closed it immediately. This was not very productive. There are lots of things that can be done after an incoming connection is established. Afterall the connection was established for the purpose of communication. So lets reply to the client.

Function sendall can be used to send something to the socket of the incoming connection and the client should see it. Here is an example :
'''

import socket
import sys

HOST = ''
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    server.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

server.listen(10)
print 'Socket now listening'

#wait to accept a connection - bloking call
conn, addr = server.accept()

print 'Connected with ' + addr[0] + ':' + str(addr[1])

#now keep talking with the client
data = conn.recv(1024)
conn.sendall(data)

conn.close()
server.close()
