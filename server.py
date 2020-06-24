import socket

s = socket.socket() #type of network you are working with, type of network 
# print(f'socket {s}')


ip = 'localhost'
port = 9999 #port no range 0 to 65535 
s.bind((ip,port)) #bind socket with port no and ip

s.listen(3) #3 connections , if we now have 4th connection it will be refused

print("Waiting for Connection") #convert string to byte

while True:
    #accept connection from client
    c,addr = s.accept() # returns client socket , address of client(IP,random Port of client)
    name = c.recv(1024).decode()

    print("Connected with addr",addr)
    
    print(f'Hey {name}')

    c.send(bytes("Welcome to mid#y world",'utf-8')) #send to client

    c.close()
