from preformatting import preformat
from temp_data import temp_data
from http.server import BaseHTTPRequestHandler, HTTPServer

# class used for creating request handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        req = self.requestline
        fixedReq = req[5 : int(len(req) - 9)]


server_address = ("", 8080)
httpd = HTTPServer(server_address, RequestHandler)

if __name__ == "__main__":
    print("running")
    httpd.serve_forever()
