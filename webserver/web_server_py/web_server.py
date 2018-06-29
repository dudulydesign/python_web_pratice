import os
import socket
import threading

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

HTML_ROOT = os.path.join(BASE_DIR, "html")

print "BASE_DIR", BASE_DIR
print "HTML_ROOT", HTML_ROOT

def handle_conn(_id, cli_sock):
  while True:

    req_data = cli_sock.recv(4096)
    if len(req_data) < 1:
      print "=" * 100
      print "Connection Lost", _id
      break

    print "[%s] req %s" % (_id, repr([req_data]))

    req_headers, req_body = req_data.split("\r\n\r\n", 1)
    req_headers = req_headers.split("\r\n")
    print "=" * 100
    print "req headers"
    for h in req_headers:
      print h 

    line1 = req_headers[0]
    http_method, path_info, http_version = line1.split(" ", 2)
    print "[%s] %s" % (http_method, path_info)
    print "=" * 100

    try:
      path = path_info.strip("/")
      if len(path) == 0:
        path = "index.html"
      html_result = "<h1>hello!</h1>"

      #filepath
      fp = os.path.join(HTML_ROOT, path)
      print "fp", fp

      #read binary
      with open(fp, "rb") as f:
        html_result = f.read()
      
      print "html_result=[%s]" % html_result

    except Exception as ex:
      print ex
      html_result = "Error! %s" % ex
    headers = []
    headers.append("HTTP/1.1 200 OK")
    headers.append("Content-Type: %s" % "text/html")
    headers.append("Content-Length: %s" % len(html_result))
    rep = "\r\n".join(headers) + "\r\n\r\n" + html_result

    print "[%s] rep=%s" % (_id, repr(rep))
    cli_sock.send(rep)

def main():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(("127.0.0.1", 8080))
  sock.listen(50)

  _id = 0

  while True:
    cli_sock, addr = sock.accept()
    print "connect...", addr, cli_sock
    _id += 1

    th = threading.Thread(target=handle_conn, args=[_id, cli_sock])
    th.setDaemon(True)
    th.start()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
