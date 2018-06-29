'''
Function socket.socket creates a socket and returns a socket descriptor which can be used in other socket related functions

The above code will create a socket with the following properties ...

Address Family : AF_INET (this is IP version 4 or IPv4)
Type : SOCK_STREAM (this means connection oriented TCP protocol)

Error handling

If any of the socket functions fail then python throws an exception called socket.error which must be caught.
'''

#handling errors in python socket programs

import socket #for sockets
import sys #for exit

try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) +' , Error message : ' + msg[1] 
    sys.exit();

print 'Socket Created'
