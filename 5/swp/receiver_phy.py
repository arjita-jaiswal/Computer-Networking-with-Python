import socket			 
import pickle

def to_receiver_dll(frame):
	s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
	port=12179
	ip = '127.0.0.1'
	s1.connect((ip, port))
	data=pickle.dumps(frame)
	s1.send(data)   
	


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
port=12178
ip ='127.0.0.1'
s.bind((ip, port))
s.listen(5)	 
s1=socket.socket()		 
port=12179
ip ='127.0.0.1'
s1.connect((ip, port))

while True: 
	c,addr=s.accept()	 
	print ('Got connection from', addr)
	while 1:
		data=c.recv(1024) 
		frame=pickle.loads(data)		
		data=pickle.dumps(frame)
		s1.send(data)
		s1.settimeout(1.0)
		try:		
			ack=s1.recv(1024).decode()
			c.send(ack.encode())
		except:
			continue
