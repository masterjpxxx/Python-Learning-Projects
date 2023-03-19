#This program is the client part of the TCP_Chat
#Step1: Import socket and threading libraries
#Step2: Define receive function that accepts messag from the server
#Step3: Define the write function to send message to the server

import socket, threading

nickname = input("Please input your nickname")

#connect to the server instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',9001))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
            
        except:
            print("Sorry an error has occured!")
            client.close()
            break
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
        

received_thread = threading.Thread(target=receive)
received_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
