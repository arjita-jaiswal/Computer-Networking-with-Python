
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),12345))
s.listen(5)
#while True:
clientSocket,address=s.accept()
msg=clientSocket.recv(1024)
l=['a','e','i','o','u']
c=0
for i in range(len(msg)):
	if msg[i] in l:
		c=c+1
clientSocket.sendall(str(c))
clientSocket.close()
