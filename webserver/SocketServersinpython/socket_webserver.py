'''
1. Create socket with socket.socket function
2. Bind socket to address+port with socket.bind function
3. Put the socket in listening mode with socket.listen function
3. Accept connection with socket.accept function
'''

#Simply socket server using threads

import socket
import sys

HOST = ''
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    server.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code :' + str(msg[0]) + ' Message ' +msg[1]
    sys.exit()
print 'Socket bind complete'

server.listen(10)
print 'Socket now listening'

while 1:
  conn, addr = server.accept()
  print 'Connected with ' + addr[0] + ':' + str(addr[1])

server.close()
