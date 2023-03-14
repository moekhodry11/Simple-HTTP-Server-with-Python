from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = ""
PORT = 8000

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # serve the index.html file by default
        try:
            # open the file in binary mode
            with open(self.path[1:], 'rb') as file:
                content = file.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))

server = HTTPServer((HOST,PORT), NeuralHTTP)
print("Server now running...")

server.serve_forever()
server.server_close()
print("Server stopped.")