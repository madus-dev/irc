import socket
import threading
  

s = socket.socket()          
  

port = 10697               
  
print_lock = threading.Lock()
s.connect(('192.168.0.32', port)) 
  
p = socket.getaddrinfo('102.168.0.32',10697)
print(p)
print (s.recv(1024)) 

def receiving_thread():
    with print_lock:
        print('Starting Receiving Thread')
        pass
    while True:
        print(s.recv(1024))

def sending_thread():
    with print_lock:
        print('Starting Sending Thread')
    f = threading.Thread(target = receiving_thread)
    f.start()
    while True:
        data = input('')
    
        if data != '':
            s.sendto(bytes(data.encode('utf-8')),('102.168.0.32',10697))

t = threading.Thread(target= sending_thread)
t.start()

