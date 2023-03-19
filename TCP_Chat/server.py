#This python program acts as a server that listens for Client connections over TCP 
#Step1: Import the socket and threading Libaries
#Step2: Define server parameters such as IP address and Port
#Step3: Define a broadcast functio that sends a message to all the clients connected
#Step4: Define a handle client function that handles client connection and asks for the user's nickname
#Step5: Define a receive function that receives the clients message 

import socket, threading

#Server Parameters for now we will be using localhost IP, change the server IP if this is deployed on separate machine

server_ip = '127.0.0.1'
port = 9001

#Bind parameters and create a server instance that listens for TCP connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen()

#Initialize clients and nicknames list
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
        
        
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames.index(index)
            broadcast(f"{nickname} left the chat.".encode('ascii'))
            nicknames.remove(nickname)
            break
        
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        
        print(f"The nickname of the clients is {nickname}")
        broadcast(f"{nickname} has joined the chat".encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        

print("Server is listineng for connections!")
receive()