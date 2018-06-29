import socket
import threading

def handle_conn(_id, cli_sock):
  while True:
    req_data = cli_sock.recv(4096) 
