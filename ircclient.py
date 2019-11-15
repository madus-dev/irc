import socket
import threading
import sys
import time
import select
from tkinter import *
from tkinter import scrolledtext


username = 'user'
server_ip = '192.168.0.32'
s = socket.socket()

#server port
port = 10697               

print_lock = threading.Lock()
p = s.connect((server_ip, port))

s.setblocking(1)
#main user window
window = Tk()
window.geometry("1000x600")
menubar = Menu(window)
window.config(menu=menubar)

#File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)
#User menu
usermenu = Menu(menubar, tearoff=0)
usermenu.add_command(label='Settings')
menubar.add_cascade(label="User", menu=usermenu)
#Send message box
txt = scrolledtext.ScrolledText(window,width=100,height=5)
txt.place(x=10, y=500)
#receive message box
output = scrolledtext.ScrolledText(window,width=120,height=30)
output.place(x=10, y=10)
#send message when send button is clicked
def clicked():
    res = username + ': ' + txt.get(1.0,END)
    s.sendto(bytes(res.encode('utf-8')),(server_ip,10697))
    txt.delete(1.0,END)
btn = Button(window, text="Send", command=clicked,width=20,height=5)
btn.place(x=820,y=500)
#shutdown connection on window close
def on_closing():
    global s
    dc = username + ' Disconnected'
    s.sendto(bytes(dc.encode('utf-8')),(server_ip,port))
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    t.join()
    window.destroy()
    exit()
window.protocol("WM_DELETE_WINDOW", on_closing)
output.insert(INSERT,s.recv(1024).decode('utf-8'))
#when enter i pressed in input box send message
def enterpress(event):
    res = username + ': ' + txt.get(1.0,END)
    s.sendto(bytes(res.encode('utf-8')),('192.168.0.32',10697))
    txt.delete(1.0,END)
window.bind('<Return>', enterpress)
#second thread to receive incoming server data
def messaging_thread():
    global s
    global output
    while True:
        (ready,_,_) = select.select([s], [], [],1)
        if (ready):
            output.insert(INSERT,s.recv(1024).decode('utf-8'))
#start second thread
t = threading.Thread(target = messaging_thread)
t.start()
#end
window.mainloop()      

        
        


