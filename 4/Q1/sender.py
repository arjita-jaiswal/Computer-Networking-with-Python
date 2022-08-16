import socket,random,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

clientSocket,address=s.accept()

class frame():
    def __init__(self,kind,seqno,ack,data):
        self.kind=kind
        self.seqno=seqno
        self.ack=ack
        self.data=data

def from_network_layer():
    a=random.randint(0,100)
    data=str((bin(a)[2:]).zfill(7))
    return dll(data)

def dll(data):
    f=frame("","","","")
    f.kind='d'
    f.data=data
    return f


def to_physical_layer(f):
    print("sending -->")
    print(f.data)
    clientSocket.send(f.kind)
    time.sleep(2)
    clientSocket.send(f.data)
    return

while True:
    d=from_network_layer()
    to_physical_layer(d)

clientSocket.close()