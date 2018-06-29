#Socket server in python using select function
#The select function is given the list of connected sockets CONNECTION_LIST. The 2nd and 3rd parameters are kept empty since we do not need to check any sockets to be writable or having errors.
#read_sockets,write_sockets,error_sockets = select(read_fds , write_fds, except_fds [, timeout]);
#https://www.binarytides.com/python-socket-server-code-example/

import socket
import select

if __name__ == "__main__":

    CONNECTION_LIST = []    #list of socket clients
    RECV_BUFFER = 4096  #Advisable to keep it as an exponent of 2
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #this has no effect, why?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)

    #add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

    print "Chat server started on port" + str(PORT)

    while 1:
        #Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

        for sock in read_sockets:
            #new connection
            if sock == server_socket:
                #Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr

            #some incoming message from a client
            else:
                #Data recieved from client, process it
                try:
                    #In windows, somtimes when a TCP program closes abruptly, 
                    #a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    #echo back the client message
                    if data:
                        sock.send('OK...' + data)
                #client disconnected, so remove from socket list
                except:
                    broadcast_data(sock, "client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
    server_socket.close()



