import socket
import time
import threading

#Default TCP IP and Port
TCP_IP = '127.2.3.4'  
TCP_PORT = 52158
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = b''

#Should we still run?
run = True

Connected = False

while run:
    try:
        data = s.recv(1024)
    except:
        s.connect((TCP_IP, TCP_PORT))
        data = s.recv(1024)
        Connected = True

    print("Looking for job...")
    if data == b'T':
        run = False
        break
    ui = input("Found Job, Accept? y/n\n")

    if ui in ["y","Y"]:
        s.send(b'Yes')
        time.sleep(1)
        s.send(b'done')
        print("Job finished")
    else:
        s.send(b'No')
        time.sleep(1)
        print("Job refused")
    
