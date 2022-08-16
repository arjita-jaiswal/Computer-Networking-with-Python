import socket,shutil,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

#while True:
clientSocket,address=s.accept()
print('in main server')
name="a.txt"
path=os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(path):
        if name in files:
        	os.path.join(root, name)
        	shutil.copy(name,'/home/arjita/cn/Q1/c')
        	shutil.copy(name,'/home/arjita/cn/Q1/p')
#clientSocket.send("Welcome to the main server")
clientSocket.close()
