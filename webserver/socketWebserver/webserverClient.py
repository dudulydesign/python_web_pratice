
import socket
import threading

inString = ''
outString = ''
nick = ''

def DealOut(s):
    global nick, outString
    while True:
        outString = raw_input()
        outString = nick + ':' + outString
        s.send(outString)

def DealIn(s):
    global inString
    while True:
        try:
            inString = s.recv(1024)
            if not inString:
                break
            if outString != inString:
                print inString
        except:
            break

nick = raw_input("input your nickname: ")
ip = raw_input("input the server's ip address: ")
sock = socket.socket
