import socket
import threading
import sys
import time
import select
  

s = socket.socket()


port = 10697               

print_lock = threading.Lock()
s.connect(('192.168.0.32', port))

s.setblocking(1)
print (s.recv(1024).decode('utf-8'))
def sending_thread():
    global i
    while True:
        for line in sys.stdin:
            if line !='\n':
                s.sendto(bytes(line.encode('utf-8')),('192.168.0.32',10697))
            time.sleep(0.5)
            

t = threading.Thread(target = sending_thread)
t.start()


while True:
    (ready,_,_) = select.select([s], [], [],1)
    if (ready):
        print(s.recv(1024).decode('utf-8'))
        

        
        


