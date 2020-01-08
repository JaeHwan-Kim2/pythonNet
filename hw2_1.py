import os
import socket
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

class ForkedClient():
    """ A client to test forking server"""
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def run(self):
        """ Clinet playing with the server """
        current_process_id = os.getpid()
        
        sent_data_length = self.sock.send(ECHO_MSG.encode('utf-8'))
        

        response = self.sock.recv(BUF_SIZE).decode('utf-8')
        

    def shutdown(self):
        """ Cleanup the client socket """
        self.sock.close()

class ForkingServerRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(BUF_SIZE).decode('utf-8')
        current_process_id = os.getpid()
        response = '%s : %s' %(current_process_id, data)
       
        self.request.send(response.encode('utf-8'))
        return

class ForkingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Nothing to add gere, inherited everything necessary from parents """
    pass

def main() :
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target = server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    

    client1 = ForkedClient(ip, port)
while True:
    message = input("CLIENT : ")
    
    if 'bye' in message:
                print("호스트와의 연결이 종료되었습니다....")
                exit()
    else:
        result = message.swapcase()
        print (result)
        continue

if __name__ == "__main__":
    main()
