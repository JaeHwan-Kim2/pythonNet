import sys
import socket
import argparse

def main():
    #setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action='store', dest='host', required='False')
    parser.add_argument('--port', action='store', dest='port', type=int, required="False")
    parser.add_argument('--file', action='store', dest='file', required="False")
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # First Try-Except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Error createing socket: {e}')
        sys.exit(1)      
    # Second Try-Except block -- connect to given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f'Address-related error connecting to server: {e}')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error : {e}')
        sys.exit(1) 

    # Third Try-except block -- seding data
    try:
        s.sendall(("Get : %s HTTP/1.0\r\n\r\n" % filename).encode('utf-8'))
    except socket.error as e:
        print(f"Error sending data: {e}")
        sys.exit(1)

    while 1:
        # Fourth tr-except block -- watiing to receive data from remote host
        try:
            buf = s.recv(4096)
        except socket.error as e:
            print(f'Error receiving data: {e}')   

        if not len(buf):
            break
        # write the receive data
        sys.stdout.write(buf.decode('utf-8'))

if __name__ == "__main__":
    main()