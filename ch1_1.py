import socket

def print_machine_info():
    host_name = socket.gethostname() #변수 선언. 실행 할 때 string 형태로 함수 반환값. 
    ip_address = socket.gethostbyname(host_name) #파라메타로 host_name을 넣어주면 주소값을 얻는다.
    print ("Host name : %s" %host_name)
    print ("IP address : %s" %ip_address)

if __name__ == '__main__':
    print_machine_info()