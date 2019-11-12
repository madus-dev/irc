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
    while True:
        data = input('')
    
        if data != '':
            s.sendto(bytes(data.encode('utf-8')),('102.168.0.32',10697))
            time.sleep(0.5)
            continue

t = threading.Thread(target= sending_thread)
t.start()


while True:
    (ready,_,_) = select.select([s], [], [],5)
    if (ready):
    
        print(s.recv(1024))
       

        
        


