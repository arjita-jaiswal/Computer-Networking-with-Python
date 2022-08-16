import socket			 
import pickle 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
print("Socket successfully created")
port=12180
ip ='127.0.0.1'
s.bind((ip, port))
s.listen(5)	 
print("socket is listening")			
info=""
while True: 
	c,addr=s.accept()	 
	print ('Got connection from', addr)
	while 1: 
		c.settimeout(1.0)
		try:		
			data=c.recv(1024).decode()
			if data!=info:			
				print("Received data: "+bin(int(data)).replace("0b",""))
			info=data
		except:
			continue 
	c.close() 
	
