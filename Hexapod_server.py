import time
from http.server import BaseHTTPRequestHandler, HTTPServer

Req = open("Request.txt", "w")
Req.close()
Request2 = "foo"
class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request, Request2
    messagetosend = bytes('Change it to name',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print(Request)
    global hight, speed, sleep
    if Request == Request2:
        print("all good")
    elif Request is not Request2:
        Request2 = Request
        Req = open("Request.txt", "a")
        Req.write(Request + "\n")
        Req.close()
    return


server_address_httpd = ('Change it to your ip',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting server:')
httpd.serve_forever()