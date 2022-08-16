import socket			 
import pickle

def to_receiver_phy(frame):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
	port=12178
	ip = '127.0.0.1'
	s.connect((ip, port))
	data=pickle.dumps(frame)
	s.send(data) 
	

s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
port=12177
ip = '127.0.0.1'
s1.bind((ip, port))
s1.listen(5)
s=socket.socket()		 
port=12178
ip = '127.0.0.1'
s.connect((ip, port))
		 
while True: 
	c,addr=s1.accept()	 
	print ('Got connection from', addr)
	while 1:	   
		data=c.recv(1024) 
		frame=pickle.loads(data)
		data=pickle.dumps(frame)
		s.send(data)
		s.settimeout(1.0)
		try:		
			ack=s.recv(1024).decode()
			c.send(ack.encode())
		except:
			continue


