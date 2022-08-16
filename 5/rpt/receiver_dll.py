import socket			 
import pickle
import random

def event(Frame_Arrival):
	if Frame_Arrival:
		return True
	else:
		return False	

def parity_check(data):
	count=0
	while data:
		count=count+data&1
		data=data>>1
	if count%2:
		return 1
	else:
		return 0


def from_physical_layer(): 
	s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
	port=12179
	ip = '127.0.0.1'
	s1.bind((ip, port))
	s1.listen(5)	 
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
	port=12180
	ip = '127.0.0.1'
	s.connect((ip, port))
		
	while True: 
		c,addr=s1.accept()	 
		print ('Got connection from', addr)
		ack=0
		frame_expected=1
		frame_received=0
		while 1:
			window_size=4
			while window_size:
				window_size=window_size-1
				data=c.recv(1024) 
				frame=pickle.loads(data)		
				#print("frame received with data "+packet)
				i=random.randint(1,7)
				frame_received=frame[1]
				info=frame[2]
				parity_bit=frame[3]
				cal_parity=parity_check(int(info))
				error=0
				if i!=7 and cal_parity==parity_bit:
					ack=frame_expected
					c.send(str(ack).encode())
					print("acknowledment sent")
				elif cal_parity!=parity_bit:
					c.send(str(ack).encode())	
					print("checksum_err")
					error=1
				else:					#acknowledment frame lost
					print("frame lost ")
					break
				if event(info) and error==0:   			
					s.send(info.encode())  
					frame_expected=(frame_expected+1)%8
				else:
					ack = -1
					c.send(str(ack).encode())
	

def to_network_layer(packet):
	s=socket.socket()		 
	port=12180
	ip = '127.0.0.1'
	s.connect((ip, port))
	s.send(packet.encode())  

from_physical_layer()
	

 
	
