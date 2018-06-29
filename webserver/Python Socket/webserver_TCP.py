
import socket, threading, time
 
size = 1024
host = '127.0.0.1'

port = 8099
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
 
sock.listen(5)
print('wait...')
 
 
def tcpLink(sock, addr):
    print('sock:', type(sock))
    print('addr:', type(addr))
    print('Accept new connection from %s:%s' % addr)
    # client connetion with server, send message to client
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode(('utf-8')) == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
 
 
# create a conn forever
while True:
    # accept a client
    socks, addr = sock.accept()
    # create a request
    t = threading.Thread(target=tcpLink, args=(socks, addr))
    t.start()
