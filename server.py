

import socket
import threading

host = 'localhost'
port = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print("Connected by client", addr[0])
data="Connect to Server"
conn.send(data.encode('utf-8'))

def snedMessage():
    while True:
        data = input()
        data = '[server] : ' + data
        data = data.encode('utf-8')
        print(data.decode('utf-8'))

        conn.send(data)
    conn.close()

def recvMessage():
    while True:
        data = conn.recv(1024)
        if not data:
            break
        else:
            data = data.decode("utf-8", "ignore")
            print("[client] : " + data)
    conn.close()

threading._start_new_thread(snedMessage, ())
threading._start_new_thread(recvMessage, ())

while True:
    pass