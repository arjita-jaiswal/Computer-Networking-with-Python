import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
l=(raw_input("Enter IP and port:"))
p=input()
s.connect((l,p))
m=raw_input("Enter string:")
s.send(m)
print(s.recv(1024))