import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    """A simple echo server"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print ('Starting up echo server on {server_address} port {server_address}')
    sock.bind(server_address)

    sock.listen(backlog)
    while True:
        print ("Waiting to receive message from client")
        client, address = sock.accept()
        try:
            message = input("SERVER : ")
            data = client.recv(data_payload)
            if data:
                print(f"CLIENT : {data}")
                client.send(message.encode("utf-8"))
        except Exception as e:
            print(f"{e}")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)