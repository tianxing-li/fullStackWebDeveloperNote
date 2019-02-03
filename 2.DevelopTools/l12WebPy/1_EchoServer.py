from http.server import HTTPServer, BaseHTTPRequestHandler


class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write('Your path is: '.encode() + self.path[1:].encode())
        """
        message = self.path[1:]  # Extract 'bears' from '/bears', for instance
        message_bytes = message.encode()  # Make bytes from the string
        self.wfile.write(message_bytes)  # Send it over the network
        """

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, EchoHandler)
    httpd.serve_forever()
