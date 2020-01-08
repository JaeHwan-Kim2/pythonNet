import os 
import socket 
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """An example of threaded TCP request handler"""
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "%s : %s" %(cur_thread.name, data)
        self.request.sendall(response.encode('utf-8'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":

     server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
     ip, port = server.server_address
     print(port)

     server_thread = threading.Thread(target=server.serve_forever)
     server_thread.start()
     print ("Server loop running on thread : %s" %server_thread.name)
