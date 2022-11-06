from http.server import BaseHTTPRequestHandler
from json import dumps

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(dumps({"hello": "world!"}).encode("utf8"))
        except Exception as err:
            print(err)