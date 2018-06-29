'''
Connect to a Server
We connect to a remote server on a certain port number. 
So we need 2 things , IP address and port number to connect to. 
So you need to know the IP address of the remote server you are connecting to. 
Here we used the ip address of google.com as a sample.

First get the IP address of the remote host/url

Before connecting to a remote host, its ip address is needed. 
In python the getting the ip address is quite simple.
'''
import socket 
import sys

try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print 'Socket Created'

host = 'www.google.com'

try:
    remote_ip = socket.gethostbyname( host )

except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'Ip address of ' + host + ' is ' + remote_ip
