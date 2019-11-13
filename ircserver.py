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
        while True:
            global ip_arr


            (data,address) = ip_arr[y - 1].recvfrom(4096)
            # if there is no longer a connection stop thread and remove ip from array
            

            print(str(data.decode('utf-8')))
            temp = data.decode('utf-8')
            temp2 = temp.split(' ')
            for f in ip_arr:
                try:
                    f.send(data)
                except:
                    pass
            if temp2[1] == 'Disconnected':
                vars()['t' + str(y)].join()

                
                
                
def connection_thread():
    global ip_arr
    global i
    global p
    while True:

        
        # Establish connection with client. 
        c, addr = s.accept()
        
        print('Got connection from', addr)

      
         # send a thank you message to the client.  
        c.send(b'Connected...')
        break
    ip_arr.append(c)
    i += 1


    message_thread(i)
connection_thread()
    

