'''
Now that we have the ip address of the remote host/system, 
we can connect to ip on a certain 'port' using the connect function.

It creates a socket and then connects. 
Try connecting to a port different from port 80 and you should not be able to connect which indicates that the port is not open for connection. 
This logic can be used to build a port scanner.
'''

#QUICK example

import socket
import sys

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to creat socket. Error code: ' + str(msg[0]) + ', Error message : ' + msg[1]
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

print 'Ip address of ' + host + ' is ' + remote_ip

#Connect to remote server
server.connect((remote_ip , port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

