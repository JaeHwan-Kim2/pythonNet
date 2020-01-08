import sys
import socket
import os

import argparse

payload = 2048

def ftp_client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    sock.connect(server_address)
    print ("서버에 연결되었습니다 :  %s " %host)
    
    while True:
        print (sock.recv(payload).decode('utf-8'))
        
        while True:
            data = input("위에서 명령어를 고르시오 : ")
            sock.send(data.encode('utf-8'))
            if 'USER' in data:
                print(sock.recv(payload).decode('utf-8'))
                password = input()
            elif data == 'PASS':
                print(sock.recv(payload).decode('utf-8'))
            elif 'ls' in data:
                print(sock.recv(payload).decode('utf-8'))
            elif 'get' in data:
                splitmsg = data.split()
                if len(splitmsg) < 2:
                    print("Too small parameter numbers %s" %splitmsg)
                    continue
                else:
                    print (sock.recv(payload).decode('utf-8'))
                    while True:
                        file = sock.recv(payload).decode('utf-8')
                        print (file)
                        name = input('파일명을 변경하시오 : ')
                        ren = open(name, 'w')
                        ren.write(file)
                        ren.close()
                        break

            elif 'bye' in data:
                print("호스트와의 연결이 종료되었습니다....")
                sock.recv(payload).decode('utf-8')
                sock.close()
                exit()
            else:
                print(sock.recv(payload).decode('utf-8'))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FTP Client Example')
    parser.add_argument('--host', action='store', dest="host", type=str, required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args() 
    host = given_args.host
    port = given_args.port
    ftp_client(host, port)