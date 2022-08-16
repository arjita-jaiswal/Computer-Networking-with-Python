import socket,shutil,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),12345))
s.listen(5)

#while True:
clientSocket,address=s.accept()
print('In proxy server')
#clientSocket.send("Welcome to the proxy server")
#clientSocket.close()
name="a.txt"
path=os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(path):
        if name in files:
        	os.path.join(root, name)
        else:
			s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s1.connect((socket.gethostname(),1234))
			print("in proxy client")
			#msg=s1.recv(1024)
			#print(msg)
			#clientSocket.send(msg)
			clientSocket.close()

