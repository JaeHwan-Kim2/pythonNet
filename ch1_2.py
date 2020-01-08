import socket

def get_remote_machine_info():
    remote_host = 'www.python.org'
    try:
        print("IP address of %s : %s" %(remote_host, socket.gethostbyname(remote_host)))
    
    except (socket.error,Exception):
        print("%s : %s" %(remote_host, Exception))

if __name__ == '__main__':
    get_remote_machine_info()
