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
        message = "Test message. This will be echoed"
        print ("Sending {message}")
        sock.sendall(message.encode())
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print ("Received : {data}")
    
    except socket.error as e:
        print ("Socket error : %s" %str(e))
    except Exception as e:
        print ("Other exception : %s" %str(e))
    finally:
        print ("Other exception to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)