import socket
import struct
import time

s=socket.socket()
port=8000
s.connect(('127.0.0.1',port))
prev_seq_num=1

def wait_for_event():
    event=s.recv(1024)
    return event

def from_physical_layer():
    d=s.recv(1024)
    x=struct.unpack('iiii',d)
    print(x)
    return x;

def to_network_layer(string):
    data=string
    print("network layer recieved data"+str(data))

def send_acknowledgment():

    ack=input("input your acknowledment..")
    s.send(ack)

flag=1
while(True):
    event=wait_for_event()

    if(event=="pkt_receieved"):
        str_recieved=from_physical_layer()
        data_rec=str_recieved[0]
        header=str_recieved[1]
        footer=str_recieved[2]
        seq_num_of_RecvStr=str_recieved[3]
        print(str(prev_seq_num)+" "+str(seq_num_of_RecvStr))
        if(prev_seq_num==seq_num_of_RecvStr):
            print("Duplicate frame")
            ack="same_frame"
            s.send(ack)
        else:
            prev_seq_num=seq_num_of_RecvStr
            send_acknowledgment()
            to_network_layer(data_rec)
        
        """if(prev_ack=="yes"):
            print("previos ack was yes...therfore ignore if more than 10sec")
            to_network_layer(data_rec)
        else:
            to_network_layer(data_rec)"""

        """if(seq_num_of_RecvStr==prev_seq_num):
            print("same string recieved again..")
        else:
            to_network_layer(data_rec)
            prev_seq_num=seq_num_of_RecvStr"""
        #to_network_layer(data_rec)


    if(flag==0):
        break

s.close()
