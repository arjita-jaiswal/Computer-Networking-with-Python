import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),12345))
print("in client")
#msg=s.recv(1024)
#print(msg)
