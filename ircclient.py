import socket
import threading
import sys
import time
import select
from tkinter import *
from tkinter import scrolledtext

username = 'Madus'
s = socket.socket()


port = 10697               

print_lock = threading.Lock()
s.connect(('192.168.0.32', port))

s.setblocking(1)
window = Tk()
window.geometry("1000x600")
txt = scrolledtext.ScrolledText(window,width=100,height=5)
txt.place(x=10, y=500)
output = scrolledtext.ScrolledText(window,width=120,height=30)
output.place(x=10, y=10)
def clicked():
    res = username + ': ' + txt.get(1.0,END)
    s.sendto(bytes(res.encode('utf-8')),('192.168.0.32',10697))
    txt.delete(1.0,END)
btn = Button(window, text="Send", command=clicked,width=20,height=5)
btn.place(x=820,y=500)


output.insert(INSERT,s.recv(1024).decode('utf-8'))


        
            

def enterpress(event):
    res = username + ': ' + txt.get(1.0,END)
    s.sendto(bytes(res.encode('utf-8')),('192.168.0.32',10697))
    txt.delete(1.0,END)
window.bind('<Return>', enterpress)
def messaging_thread():
    global s
    global output
    while True:
        (ready,_,_) = select.select([s], [], [],1)
        if (ready):
            output.insert(INSERT,s.recv(1024).decode('utf-8'))

t = threading.Thread(target = messaging_thread)
t.start()
window.mainloop()      

        
        


