import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),12345))
m=raw_input("Enter string:")
s.send(m)
#print("No of vowels="+s.recv(1024))