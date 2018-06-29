import socket
import threading

#define "handle_conn" 

def handle_conn(_id, cli_sock):
  while True:

    req_data = cli_sock.recv(4096)  #send data to client
    if len(req_data) < 1:
      print "=" * 100
      print "Connection Lost", _id
      break

    print "[%s] req %s" % (_id, repr([req_data]))

    #split data of "req_headers" and "req_body"
    req_headers, req_body = req_data.split("\r\n\r\n", 1) 
    #split data of "req_headers"
    req_headers = req_headers.split("\r\n")
    print "=" * 100

    print "req headers"
    for h in req_headers:
      print h
    print "=" * 100

    html_result = "<h1>hello!</h1>" #name "html_result"
    headers = []            #name headers is empty arrary
    headers.append("HTTP/1.1 200 OK")
    headers.append("Content-Type: %s" % "text/html") 
    headers.append("Content-Length: %s" % len(html_result)) 

    rep = "\r\n".join(headers) + "\r\n\r\n" + html_result
    print "[%s] rep=%s" % (_id, repr(rep))

    cli_sock.send(rep)

def main():

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(("127.0.0.1", 8080))
  sock.listen(5)

  _id = 0

  while True:
    cli_sock, addr = sock.accept()
    print "connect...", addr, cli_sock
    _id += 1
    print "=" * 100

    th = threading.Thread(target=handle_conn, args=[_id, cli_sock])
    th.setDaemon(True)
    th.start()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass


