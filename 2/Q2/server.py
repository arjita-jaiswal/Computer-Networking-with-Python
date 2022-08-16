import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
#while True:
clientSocket,address=s.accept()
date=clientSocket.recv(1024)
dd,mm,yy=date.split("/")
dd=int(dd)
mm=int(mm)
yy=int(yy)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    max1=29
else:
    max1=28
if(mm<1 or mm>12):
    clientSocket.sendall("0")
elif(dd<1 or dd>max1):
    clientSocket.sendall("0")
else:
    clientSocket.sendall("1")
clientSocket.close()
