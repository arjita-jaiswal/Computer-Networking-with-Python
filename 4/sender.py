import socket
from threading import *
import struct
import signal
import sys, select
import time

TIMEOUT = 5 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000

s.bind((host, port))
s.listen(5)

c,addr=s.accept()
seq_number=0

def from_network_layer():

    #input only corresponding data here

    data=int(input('input your data here..'))
    check_sum=(int(str(data),2))
    global seq_number
    seq_number=abs(seq_number-1)
    return data,check_sum



def to_physical_layer(strin,seq_num):

    abc="pkt_receieved"
    c.send(abc)
    header=10
    footer=11
    check_sum=(int(str(strin),2))
    packet=struct.pack('iiii',strin,header,check_sum,int(seq_num))
    c.send(packet)

def wait_for_event():
    t1=time.time()
    acknow=c.recv(1024)
    t2=time.time()

    if(t2-t1>10):
        return acknow,True
    else:
        return acknow,False

flag=1
while(True):

    if(flag==1):

        string,seq_num=from_network_layer()
        
        seq_number=1-seq_number
        to_physical_layer(string,seq_number)
        last_data=string
        last_seq=seq_num

    else:
        seq_num=to_physical_layer(last_data,seq_number)

    ack,boolean=wait_for_event()

    if(boolean):
        print("lost frame..send again")
        flag=0
        last_data=string

    else:
        if(ack=="yes"):
            flag=1
            print("frame received")
        if(ack=="check_err"):
            print("Frame has checksum error")
        if(ack=="same_frame"):
            flag=1
            print("send the next frame")

    if(string=="over"):
        break

c.close()


	

