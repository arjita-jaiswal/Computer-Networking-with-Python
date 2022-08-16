import socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

clientSocket,address=s.accept()

class frame():
    def __init__(self,seqno,ackno,data):
        self.seqno=seqno
        self.ackno=ackno
        self.data=data

def from_network_layer():
    print("Enter data to send")
    data=raw_input()
    return data

def to_physical_layer(f):
    print("sending data to to_physical_layer")
    print(str(f.seqno))
    print(str(f.data))
    clientSocket.send(str(f.seqno))
    clientSocket.send(str(f.data))
    return

def wait_for_event():
    while True:
        try:
            clientSocket.settimeout(10.0)
            e=clientSocket.recv(1024)
        except:
            break
        if(e):
            return e
        else:
            return "timeout"


    #now=time.time()
    #future=now+20
    #while time.time()<future:
     #   e=clientSocket.recv(1024)
     #   return e

def from_physical_layer():
    a=clientSocket.recv(1024)
    return a

f=frame("","","")
next_frame_to_send=1
d=from_network_layer()
while True:
    f.data=d
    f.seqno=next_frame_to_send
    to_physical_layer(f)
    print("wait_for_event")
    event=wait_for_event()
    print(event)
    if(event=='frame_arrival'):
        a=from_physical_layer()
        if(int(a)==next_frame_to_send):
            next_frame_to_send=next_frame_to_send+1

    elif(event=='timeout'):
        print("sending frame again because timeout")
        continue

clientSocket.close()