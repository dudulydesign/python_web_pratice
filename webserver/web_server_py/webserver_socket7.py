'''
Receiving Data
Function recv is used to receive data on a socket. 
In the following example we shall send the same message as the last example and receive a reply from the server.
'''

#Socket client example in python 

import socket
import sys

#Create an INET, STREAMing socket
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
  print 'Failed to create socket'
  sys.exit()

print 'Socket Created'

host = 'www.google.com';
port = 80;

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
  #could not resolve
  print 'Hostname could not be resolved. Exiting'
  sys.exit()

#Connect to remote server
server.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

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

#Now receive data
reply = server.recv(4096)
print reply

'''
Close socket
Function close is used to close the socket.
'''
server.close()


'''
So in the above example we learned how to :
1. Create a socket
2. Connect to remote server
3. Send some data
4. Receive a reply
'''
