import http.server

class HelloHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        #handler class, inherits from the BaseHTTPRequestHandler (Defined in http.server)
        
        # 1. send rsp
        self.send_response(200)

        # 2. send headers
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # 3. send rsp body
        self.wfile.write("Hello, here is Server Response!\n".encode())
            # self.wfile is a variable, wfile stands for writeable file.
            # send a string over the HTTP connection, have to encode the string into a bytes object.(https://docs.python.org/3.6/howto/unicode.html)

        
if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = http.server.HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()