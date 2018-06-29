# client send data to server
import socket
 
host = '127.0.0.1'
port = 8099
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conn with server
client.connect((host, port))
 
try:
    while True:
        msg = b"\n test"
        #  send data to server
        client.sendall(msg)
        data = client.recv(1024)
        print(data)
except socket.errno as e:
    print("socket error: %s" % e)
finally:
    client.close()
