'''
TCP Client sample
'''

import socket

target_host = ''
target_port = 9999

#create socket
#AF_INET means a IPv4 link or a name of server
#SOCK_STREAM means this is a TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#create a client connection
client.connect((target_host, target_port))

#send a data to target
client. send("GET / HTTP/ 1.1\r\n Host:www.google.com\r\n\r\n")

#recieve data
response = client. recv(4096)

print response
