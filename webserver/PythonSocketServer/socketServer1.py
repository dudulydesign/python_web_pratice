
import socket
import sys
#======================================
HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
#======================================

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code:' + str(msg[0]) + 'Message' + msg[1]
    sys.exit()
print 'Socket bind complete'

#======================================

#監聽連接
s.listen(10)
print 'Socket now listening'

#======================================

#now keep talking with the client
while 1:

    #接收連接
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    #======================================

    #display client information
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #======================================

    data = conn.recv(1024)
    reply = 'OK...' + data
    if not data:
        break
    conn.sendall(reply)

conn.close()
s.close()

