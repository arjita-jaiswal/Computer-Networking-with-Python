import socket			 
import pickle
import random
import time
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
		st=0
		end=4
		while 1:
			window_size=4
			seq=st
			end=(seq+4)%8
			while window_size:
				frame=[]
				kind=1
				info=c.recv(1024).decode()	
				print("Sending frame with seq no "+str(seq))
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
				seq=(seq+1)%8
				window_size=window_size-1
			s.settimeout(1.0)
			window_size=4
			temp=st
			while window_size:
				window_size=window_size-1
				try:		
					ack=s.recv(1024).decode()

					# if ack==-1:
					# 	print("negative acknowledgement received resind the frame")
				except:

					break
			i=random.randint(1,4)
			if(i!=4):
				i=st
				while 1:
					print("Acknowledgement recieved for frame "+str(i))
					i=(i+1)%8
					if i==(end)%8:
						break
					time.sleep(0.5)
				st=end
			else:
				i=random.randint(1,3)
				while i:
					i=i-1
					print("Acknowledgement recieved for frame "+str(st))
					st=(st+1)%8
					time.sleep(0.5)	
				print("Acknowledgement not recieved for frame "+str(st))
			# if ack==-1:
			# 	st=temp
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

 
	
