'''
Sending Data
Function sendall will simply send data.
Lets send some data to google.com
'''

import socket
import sys

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print 'Socket Created'

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname( host )

except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print ' Ip address of ' + host + ' is ' + remote_ip

#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    #Set the whole string
    server.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()

print 'Message send successfully'
