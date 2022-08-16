import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),12346))
s.listen(5)

#while True:
clientSocket,address=s.accept()
print('in main server')
msg=clientSocket.recv(1024)
d=[]
with open("Department.txt") as f1:
	for line in f1:
		line = line.replace("\n", "")
		d.append(line.split(" "))
f1.close()
e=[]
with open("Employee.txt") as f2:
	for line in f2:
		line = line.replace("\n", "")
		e.append(line.split(" "))
if (msg=='a'):
	max_s=0
	p=0
	for i in range(len(e)):
		if(max_s<int(e[i][1])):
			max_s=int(e[i][1])
			p=i
	clientSocket.send("Name : "+str(e[p][0])+"\n"+"Salary : "+str(e[p][1])+"\n"+"Department : "+str(e[p][2]))
elif(msg=='b'):
	clientSocket.send("Enter Department :")
	d1=clientSocket.recv(1024)
	print d1
	for i in range(len(e)):
		if(e[i][2]==d1):
			clientSocket.send("Name : "+str(e[i][0])+"\n"+"Salary : "+str(e[i][1])+"\n"+"Department : "+str(e[i][2])+"\n")
elif(msg=='c'):
	max_e=0
	q=0
	for k in range(len(d)):
		if(max_e<int(d[k][1])):
			max_e=int(d[k][1])
			q=k

	for j in range(len(e)):
		if(e[j][2]==d[q][0]):
			clientSocket.send("Name : "+str(e[j][0])+"\n"+"Salary : "+str(e[j][1])+"\n"+"Department : "+str(e[j][2])+"\n")	

elif(msg=='d'):
	def secondelement(ele):
		return int(ele[1])
	e.sort(key=secondelement,reverse=True)
	store=[]
	for i in range(len(e)):
		store.append(int(e[i][1]))
	l=store[0]
	for j in range(len(store)):	
		if(l!=store[j]):
			l=store[j]
			break
	for j in range(len(e)):
		if(int(e[j][1])==l):
			clientSocket.send("Name : "+str(e[j][0])+"\n"+"Salary : "+str(e[j][1])+"\n"+"Department : "+str(e[j][2])+"\n")
else:
	clientSocket.send("Exit")
clientSocket.close()
