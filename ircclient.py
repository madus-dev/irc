import socket                
  

s = socket.socket()          
  

port = 10697               
  

s.connect(('192.168.0.32', port)) 
  

print (s.recv(1024)) 
while True:
    data = input('')
    
    if data != '':
        s.sendto(bytes(data.encode('utf-8')),(socket.gethostname(),10697))
