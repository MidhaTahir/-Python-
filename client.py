import socket

c = socket.socket()

c.connect(('localhost',9999)) #ip address of server, and port no of server to connect with 

name = input("Enter your name: ") 
c.send(bytes(name,'utf-8')) #send to server

print(c.recv(1024).decode()) #receives in a buffer