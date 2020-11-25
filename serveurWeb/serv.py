# Python 3 server example
import http.server
import socketserver
import os

serverPort = 8080
os.chdir("../clientWeb")
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('content-type', 'text/html')
		self.end_headers()

	def do_get(self):
		size = int(self.header.getheader('content-legth',0))
		body = self.rfile.read(size)
		#print(body)
		return http.server.SimpleHTTPRequestHandler.do_GET(self)

	def do_post(self):
		self._set_headers()
		size = int(self.header.getheader('content-legth',0))
		body = self.rfile.read(size)
		#print(body)
		#call treatment function
		return('request processed')

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("",serverPort),Handler) as httpd:
	print("Http Server Serving at port", serverPort)
	httpd.serve_forever()

