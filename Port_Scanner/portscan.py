#This python program scans for open ports in the specified IP Address
#Step1: Import Socket, Threading libraries
#Step2: Create scan method
#Step3: Use threading and queue to run the process faster
#Step4: Display the open ports

import socket, threading
from queue import Queue


queue = Queue()
open_ports = []
target_ip = input("Input the target IP Address: ")
#target_ip = '192.168.1.4'
def portscan(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        return True
    except:
        return False
    

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)
        
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(target_ip, port):
            print(f"Port {port} is open!")
            open_ports.append(port)
        else:
            print(f"Port {port} is closed!")

port_list = range(1, 200)
fill_queue(port_list)

thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    
for thread in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()
    
print(f"The open ports are: {open_ports}")
        