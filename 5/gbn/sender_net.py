import socket			 
import random
import time
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
port=12176
ip = '127.0.0.1'
s.connect((ip, port))
while 1:
	packet=random.randint(0,100)
	print("Sending "+bin(packet).replace("0b",""))  
	s.send((str(packet)).encode())
	time.sleep(1)
s.close()	 

