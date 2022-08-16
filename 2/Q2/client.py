import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
m=raw_input("Enter string:")
s.send(m)
ms=s.recv(1024)
if int(ms)==1:
	print("It is a valid date.")
elif int(ms)==0:
	print("It's an invalid date.")
