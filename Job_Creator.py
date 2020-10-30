import socket

TCP_IP = '127.2.3.4'  
TCP_PORT = 52158        
run = True
jobs = 3
data = b''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
#I was having issues with using the with keyword
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
HASC = False
while(run):
    if not HASC:
        print("Looking for seekers...\n")
        s.listen()
        print("Found seeker!\nAwaiting confirmation...\n")
        conn, addr = s.accept()
        data =b''
        HASC = True
        
    conn.send(b'Here is a job')
    while True:
            data = conn.recv(1024)
            if data == b'No':
                print("Job refused :(")
                break
            else:
                conn.recv(1024)
                print("Job Complete")
                jobs-=1
                break
    if jobs <=0:
        conn.send(b'T')
        run = False
            
            
