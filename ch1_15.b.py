import socket 
import sys

import argparse

host = 'localhost'

def echo_client(port):
    """A simple echo client"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print ("Connecting to {server_address} port {server_address}")
    sock.connect(server_address)

    try:
        message = input("CLIENT : ")
        print (f'CLIENT {message}')
        sock.sendall(message.encode("utf-8"))
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print ("Received : {data}")
    
    except socket.error as e:
        print (f"Socket error : {e}")
    except Exception as e:
        print (f"Other exception : {(str)(e)}")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)