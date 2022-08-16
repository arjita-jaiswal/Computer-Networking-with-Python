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
	

def from_network_layer(): 
	s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
	port=12176
	ip = '127.0.0.1'
	s1.bind((ip, port))
	s1.listen(5)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
	port=12177
	ip = '127.0.0.1'
	s.connect((ip, port))
	while True: 
		c,addr=s1.accept()	 
		print ('Got connection from', addr)
		seq=0
		ack=0
		while 1:
			frame=[]
			kind=1
			seq=(seq+1)%2
			info=c.recv(1024).decode()	
			#print("Sending frame with data "+info)
			if event(info):
				frame.append(kind)
				frame.append(seq)
				frame.append(info)
				parity_bit=parity_check(int(info))
				i=random.randint(1,7)
				if i==7:                        #to produce error
					parity_bit=(parity_bit+1)%2		
				frame.append(parity_bit)
				data=pickle.dumps(frame)
				s.send(data)
			s.settimeout(1.0)
			while 1:
				try:		
					ack=s.recv(1024).decode()
					print("Ack recieved "+str(ack))
					break					
				except:
					print("Acknowledgement Not recieved...")
					print("Resending the frame ")
					s.send(data)			
		c.close()

def to_physical_layer(frame):	
	s=socket.socket()		 
	port=12177
	ip = '127.0.0.1'
	s.connect((ip, port))
	data=pickle.dumps(frame)
	s.send(data)  
	flag=0 


from_network_layer()

 
	
