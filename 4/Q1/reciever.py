import socket,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

class frame():
    def __init__(self,kind,seqno,ack,data):
        self.kind=kind
        self.seqno=seqno
        self.ack=ack
        self.data=data

def dll(f):
	d=f.data
	return d

def from_physical_layer():
	k=s.recv(1024)
	d=s.recv(1024)
	f=frame("","","","")
	f.kind=k
	f.data=d
	return dll(f)


def to_network_layer(data):
	print("Received --> ")
	print(data)
	return

def wait_for_event():
	#if (s.recv(1024)):
	return 'frame_arrival'

while True:
	if(wait_for_event() == 'frame_arrival'):
		d=from_physical_layer()
		to_network_layer(d)
	#time.sleep(10)

s.close()