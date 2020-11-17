# Python 3 server example
import http.server
import socketserver
import os

serverPort = 8080
os.chdir("../clientWeb")
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_get(self):
		self.path = 'index.html'
		return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("",serverPort),Handler) as httpd:
	print("Http Server Serving at port", serverPort)
	httpd.serve_forever()

