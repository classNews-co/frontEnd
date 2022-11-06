from http.server import BaseHTTPRequestHandler
from os import getenv
from json import dumps

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            path = self.path
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(dumps({"path": path, "hello": "world!"}).encode("utf8"))
        except Exception as err:
            if getenv("DEBUG") == "true":
                self.send_error(500, str(err))
            else:
                self.send_error(500, '{"error": "Internal Server Error"}')