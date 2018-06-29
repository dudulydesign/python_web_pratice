
'''
TCP/IP Server sample

用 AF_INET 和 SOCK_STREAM 宣告這是 TCP / IPv4 的連線，並且連線限制為 5，while 開始迴圈等待連線，並且啟動 client_handler 處理用戶的資料存放到 client(socket info) , addr(remote info)，使用 thread 建立新的連線

handle_client 則處理用戶端的 request 並且發一則訊息給用戶端。
'''

import socket
import threading

bind_ip = ''
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip, bind_port)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request

    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print "[*] Acepted connection from : %s:%d" % (addr[0],addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
