'''
Before you begin
This tutorial assumes that you already have a basic knowledge of python.

So lets begin with sockets.

Creating a socket
This first thing to do is create a socket. The socket.socket function does this.
Quick Example :
'''

#socket client example in python

import socket

#creat an AF_INET, STREAM socket(TCP)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'Socket Created'
