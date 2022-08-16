import socket,random
#from random import randint
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),12345))
s.listen(5)
#while True:
clientSocket,address=s.accept()
msg=clientSocket.recv(1024)
print(msg)
n=random.randint(0,len(msg))
print n

clientSocket.close()