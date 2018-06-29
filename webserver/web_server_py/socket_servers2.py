'''
Accept connection
Function socket_accept is used for this.
'''

import socket
import sys

HOST = ''
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    server.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

server.listen(10)
print 'Socket now listening'

#wait to accept a connection - blocking call
conn, addr = server.accept()

#display client information
print 'Connected with ' + addr[0] + ':' + str(addr[1])

