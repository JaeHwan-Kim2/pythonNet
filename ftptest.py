import ftplib
import sys
import os


address = input('서버 주소 입력 : ')
port = input('포트 번호 입력 : ')
id = input('사용자 계정 입력 : ')
password = input('사용자 암호 입력 : ')
ftp = ftplib.FTP(address)
ftp.login(id, password)


print ("환영합니다. 서버에 연결되었습니다.")
cd = input('작업을 입력하세요 : ')
ftp.cwd(cd)


def upload(ftp):
    filename = input('업로드할 파일 : ')
    ftp.storbinary("STOR " + filename, open(filename, "rb"), 1024)
def download(ftp):
    filename = input('다운로드할 파일 : ')
    ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
def showfiles(ftp):
    filelist = []
    ftp.dir(filelist.append)
    print(cd, '파일 목록 = ', filelist)



while True:
    print('업로드 - up / 다운로드 - down / 파일 목록 보기 - file')
    job = input('작업을 선택 : ')
    if job == 'up':
        upload(ftp)
    elif job == 'down':
        download(ftp)
    elif job == 'file':
        showfiles(ftp)
    else :
        print('서버와의 연결이 종료되었습니다.')
        ftp.quit()
        break