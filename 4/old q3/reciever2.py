import socket
import struct

s=socket.socket()
port=8008
s.connect(('127.0.0.1',port))

def wait_for_event():
    d=s.recv(1024)
    event=d.decode("utf-8")
    return event

def from_physical_layer():
    d=s.recv(1024)
    x=struct.unpack('iiii',d)
    print(x)
    return x;

def to_network_layer(string):
    data=string

def send_acknowledgment():

    ack=input()
    s.send(bytes(ack,"utf-8"))

flag=1
while(True):
    event=wait_for_event()

    #print(event)

    if(event=="pkt_receieved"):
        str_recieved=from_physical_layer()
        
        send_acknowledgment()

        data_rec=str_recieved[0]
        header=str_recieved[1]
        footer=str_recieved[2]
        
        to_network_layer(data_rec)

    if(flag==0):
        break

s.close()
