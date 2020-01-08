# Python socket FTP Server tester for ver 3.7.

import socket
import sys
import os

import argparse

host = 'localhost'
data_payload = 2048
backlog = 1

def ftp_server(port):
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up Experimental FTP server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog) 
    
    while True: 
        print ("Waiting to receive message from client")
        client, address = sock.accept() 
        respmsg = '''
                    Welcome to the Experimental FTP Server
                    This FTP server is only response to limited commands:
                    USER, PASS, ls, get, bye
                    **TO END client, MUST type "bye"**
                '''
        print(respmsg)
        
        client.send(respmsg.encode('utf-8') )

        # process 1 connected client
        while True:
            data = client.recv(data_payload).decode('utf-8')
            if data:
                print ("Data: %s" %data)
                if 'USER' in data:
                    respmsg = 'Type Password '
                    client.send(respmsg.encode('utf-8'))
                elif 'PASS' in data:
                    respmsg = 'You are connected, Please use server carefully and enjoy it!'
                    client.send(respmsg.encode('utf-8'))
                elif 'ls' in data:
                    listoffolder = os.listdir("./")          
                    respmsg = ' '.join(listoffolder)        # join list elements to string
                    client.send(respmsg.encode('utf-8'))
                elif 'get' in data:
                    splitmsg = data.split()
                    if len(splitmsg) < 2:
                        print("Too small parameter numbers %s" %splitmsg)
                        continue
                    else:
                        print(splitmsg)
                        fileSize = os.path.getsize(splitmsg[1])
                        respmsg = 'file size ' + str(fileSize) + ' bytes'
                        client.send(respmsg.encode('utf-8'))
                    
                    try:
                        file = open(splitmsg[1], "r")
                    except Exception as id:
                        respmsg = str(id)+splitmsg[1]
                        client.send(respmsg.encode('utf-8'))
                        continue

                    while True:
                        line = file.readline()        # read line-by-line using f.readline()
                        if not line: break
                        client.send(line.encode('utf-8'))

                elif 'bye' in data:
                    respmsg = 'Bye, You disconnected'
                    client.send(respmsg.encode('utf-8'))
                    break
                else:
                    respmsg = 'Incorrect message, please type command in Welcom message'
                    client.send(respmsg.encode('utf-8'))

                #print ("sent %s bytes back to %s" % (data, address))
            # end connection
        client.close()     
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FTP Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args() 
    port = given_args.port
    ftp_server(port)
