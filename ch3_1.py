import subprocess

for lastAddr in range(1, 10):
    address = "127.0.0." + str(lastAddr)
    res = subprocess.call(['ping', '-n', '3', address])

    if res == 0:
        print ("ping to",address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")