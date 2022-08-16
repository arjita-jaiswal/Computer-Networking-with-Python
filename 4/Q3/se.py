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


def checksum(data):
    sum=bin(int(data[0],2))
    for i in range(1,len(data)):
        sum=bin(int(sum,2)+int(data[i],2))
    s=sum.replace("1","f")
    s1=s.replace("0","1")
    s2=s1.replace("f","0")
    return s2[2:]

        #sum = bin(int(num1,2) + int(num2,2))
def from_network_layer():
    a=random.randint(0,100)
    data=str((bin(a)[2:]).zfill(7))
    return data

def to_physical_layer(f):
    print("sending -->")
    print(f.data)
    clientSocket.send(f.data)
    time.sleep(2)
    #print("seqno "+str(f.seqno))
    clientSocket.send(str(f.seqno))
    time.sleep(2)
    clientSocket.send(checksum(f.data))
    return

def wait_for_event():
    global ac
    ac=clientSocket.recv(1024)
    if((time.time()-t)>5):
        return "timed out"
    else:
        return "frame_arrival"


def from_physical_layer():
    #ack=clientSocket.recv(1024)
    f.ack=int(ac)
    print("Recieved ack")
    print(f.ack)
    return

#data link layer   
global t
global next_frame_to_send
next_frame_to_send=0
global f
f=frame("","","","")
while True:
    flag=0
    d=from_network_layer()
    while True:
        f.data=d
        f.seqno=next_frame_to_send
        to_physical_layer(f)
        t=time.time()
        event=wait_for_event()
        if(event=="frame_arrival"):
            from_physical_layer()
            if(f.ack==next_frame_to_send):
                next_frame_to_send=next_frame_to_send+1
                break
            #else:
             #   continue
        elif(event=="timed out"):
            print(event)
            continue
        pass
#time.sleep(10)
clientSocket.close()
