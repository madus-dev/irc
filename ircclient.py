import socket
import threading
import sys
import time
  

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)          
  

port = 10697               
  
print_lock = threading.Lock()
s.connect(('192.168.0.32', port)) 
  


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
    z = s.recv(1024).decode('utf-8')
        
    print(z)
        
        


