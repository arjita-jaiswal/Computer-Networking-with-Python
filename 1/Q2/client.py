import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),12346))
print("in client")
o=raw_input("Enter options:")
s.sendall(o)
#while(True):
ms=s.recv(1024)
if(ms=="Enter Department :"):
	p=raw_input("Enter Department :")
	s.sendall(p)
	print(s.recv(1024))
else:
	print(ms)
