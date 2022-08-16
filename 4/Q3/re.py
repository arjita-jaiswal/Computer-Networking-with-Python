import socket
import time
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

class frame():
    def __init__(self,kind,seqno,ack,data):
        self.kind=kind
        self.seqno=seqno
        self.ack=ack
        self.data=data

def chk_error(data,check_sum):
	sum=bin(int(data[0],2))
	for i in range(1,len(data)):
		sum=bin(int(sum,2)+int(data[i],2))
	err=bin(int(sum,2)+int(check_sum,2))
	e=err[2:]
	e=e.replace("1","f")
	e=e.replace("0","1")
	e=e.replace("f","0")
	if(int(e,2)==0):
		return True
	else:
		return False

def from_physical_layer():
	d=s.recv(1024)
	error_gen=random.randint(0,5)
	if(error_gen==2):
		f.data=d.replace("1","0")
	else:
		f.data=d

	#print("Received data in PL "+f.data)
	f.seqno=s.recv(1024)
	#print("Received seqno in PL "+f.seqno)
	global check_sum
	check_sum=s.recv(1024)
	return


def to_network_layer():
	print("Received NL--> ")
	print(f.data)
	return

def wait_for_event():
	#if (s.recv(1024)):
	return 'frame_arrival'

def to_physical_layer():
	n=random.randint(0,6)
	time.sleep(n)
	print("Sending ack "+str(f.ack))
	s.send(str(f.ack))
	#if(n>5):
	#	s.send(str(f.ack))
	return

global f
f=frame("","","","")
global frame_expected
frame_expected=0
#while True:
while True:
	event=wait_for_event()
	if(event=="frame_arrival"):
		from_physical_layer()
		if(chk_error(f.data,check_sum)):
			if(f.seqno==str(frame_expected)):
				to_network_layer()
				frame_expected=frame_expected+1
			else:
				print("Duplicate frame")
				s.send(str(f.ack))
				continue
			f.ack=frame_expected-1
			to_physical_layer()
		else:
			print("Checksum Error")
			s.send(str(f.ack))
			continue

	pass

s.close()
