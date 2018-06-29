import socket
import sys

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
sock.bind(('', 54321))
sock.listen(5)
sock.settimeout(10)

while True:
    (csock, adr) = sock.accept()
    print "Client Info: ", csock, adr
    msg = csock.recv(1024)
    if not msg:
        pass
    else:
        print "Client send: " + msg
        csock.send("Hello I'm Server.\r\n")
    sock.close()
