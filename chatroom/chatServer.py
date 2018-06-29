__author__ = ''

import socket
import select

HOST = ''
PORT = 908
BACKLOG = 100
BUFF = 1024
ADDR = (HOST, PORT)

CONNECT_MAP = {}

def broadcast_msg(_srv_sock, my_sock, msg):
    for _file_no, _sock in CONNECT_MAP.iteritems():
        if _sock != _srv_sock and _sock != my_sock:
            try:
                _sock.send(msg)
            except socket.error:
                pass

def chat_server():
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind(ADDR)
    srv_sock.listen(BACKLOG)

    _epoll = select.epoll()
    _epoll.register(srv_sock.fileno(), select.EPOLLIN)

    print "Start chat server on port %d" % PORT

    while True:
        events = _epoll.poll(timeout=0.5)
        for _file_no, event in events:
            if _file_no == srv_sock.fileno():
                _cli_sock, _addr = srv_sock.accept()
                _cli_sock.setblocking(0)
                print "Client (%s, %s) connected" % _addr
                broadcast_msg(srv_sock, _cli_sock, "[%s:%s] entered root\n\r" % _addr)
                _epoll.register(_cli_sock.fileno(), select.EPOLLIN)
                CONNECT_MAP[_cli_sock.fileno()] = _cli_sock
            elif event & select.EPOLLIN:
                try:
                    _sock = CONNECT_MAP[_file_no]
                    _data = _sock.recv(BUFF)
                    if _data:
                        _msg = "<" + str(_sock.getpeername()) + ">" + _data + '\n\r'
                        broadcast_msg(
