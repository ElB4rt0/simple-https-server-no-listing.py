
#!/usr/bin/env python3
import http.server
import ssl

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'Index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

httpd = http.server.HTTPServer(('0.0.0.0', 443), handler_object)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./ssl/cert.pem', keyfile='./ssl/key.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLSv1_2)
httpd.serve_forever()
