import socket,time,random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

class frame():
	def __init__(self,seqno,ackno,data):
		self.seqno=seqno
		self.ackno=ackno
		self.data=data



def from_physical_layer():
	seq=s.recv(1024)
	data=s.recv(1024)
	print("data Received")
	return seq,data

def to_network_layer(data):
	print("Received => "+data)
	return

def wait_for_event():
	print("Frame kind:")
	event=raw_input()
	return event

def to_physical_layer(ack):
	s.send(str(ack))
	return


f=frame("","","")
frame_expected=1
i=1

while True:
	e=wait_for_event()
	if(e=='data'):
		sn,d=from_physical_layer()
		f.data=d
		f.seqno=int(sn)
		print(f.data)
		print(f.seqno)

		if (f.seqno==frame_expected):
			print("bn")
			to_network_layer(d)
			print("cn")
			to_physical_layer('frame_arrival')
			frame_expected=frame_expected+1
			print("frame_e"+str(frame_expected))
		ack=frame_expected-1
		print(ack)
		print("Sending acknowledgement")
		to_physical_layer(ack)

s.close()