import socket
from http.server import HTTPServer, BaseHTTPRequestHandler


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _send_ok(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_GET(self):
        self._send_ok()

        message = "Hello client!\r\n\r\n"
        self.wfile.write(bytes(message, "utf8"))
    
    def do_POST(self):
        data_len = int(self.headers['Content-Length'])
        data = self.rfile.read(data_len)
        
        self.log_message(f'Received {len(data)} bytes')
        self._send_ok()

        message = f"Received {len(data)} bytes from client\r\n\r\n"
        self.wfile.write(bytes(message, "utf8"))


if __name__ == '__main__':
    server = HTTPServer(('', 8000), HTTPRequestHandler)
    server.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 0)
    server.serve_forever()
