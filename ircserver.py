import socket
import threading
import time
  

s = socket.socket()          
print("Socket successfully created")

port = 10697

s.bind(('', port)) 
print ("socket binded to %s" %(port)) 

s.listen(5)     
print ("socket is listening")
ip_arr = []
i = 0
time_end = time.time() + 10
dataglob = b''
def message_thread(y):
    if i == 0:
        connection_thread()
    else:
        vars()['t'+ str(i)] = threading.Thread(target = connection_thread)
        vars()['t'+ str(i)].start()
        print('starting messaging thread...')
        x = ip_arr[y - 1]
        while True:


            (data,address) = x.recvfrom(4096)

            

            print(str(data.decode('utf-8')),x)
                
                
def connection_thread():
    global ip_arr
    global i
    while True:

        
        # Establish connection with client. 
        c, addr = s.accept()
        
        print('Got connection from', addr) 
      
         # send a thank you message to the client.  
        c.send(b'Connected...')
        break
    ip_arr.append(c)
    i += 1
    print(i)
    print(ip_arr)
    message_thread(i)
connection_thread()
    

