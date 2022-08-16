
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),12345))
print(socket.gethostbyname(socket.gethostname()))
s.listen(5)
#while True:
clientSocket,address=s.accept()
msg=clientSocket.recv(1024)
if msg.isdigit():
	while (True):
		if(len(msg)!=1):
			l=0
			for i in range(len(msg)):
				l=l+int(msg[i])
			msg=str(l)
			clientSocket.sendall(msg+"\n")
		elif(len(msg)==1):
			break
else:
	clientSocket.sendall("Sorry, cannot compute!")
clientSocket.close()
