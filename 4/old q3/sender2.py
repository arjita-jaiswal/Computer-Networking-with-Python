import socket
from threading import *
import struct
import signal
import sys, select
import time

TIMEOUT = 5 # number of seconds your want for timeout

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8008

s.bind((host, port))
s.listen(5)

c,addr=s.accept()

def from_network_layer():
    data=int(input('input your data here..'))
    return data


"""def interrupted(signum, frame):
    "called when read times out"
    print('interupted!')

signal.signal(signal.SIGALRM, interrupted)

def new_input():
    try:
            print('You have 5 seconds to type in your stuff...')
            foo = input()
            return foo
    except:
            # timeout
            return """

def to_physical_layer(strin):

    abc="pkt_receieved"

    c.send(bytes(abc,"utf-8"))

    header=10
    footer=11

    packet=struct.pack('iiii',strin,header,footer,0)
    c.send(packet)

def wait_for_event():
    t1=time.time()
    acknow=c.recv(1024).decode("utf-8")
    t2=time.time()
    if(acknow=="yes"):
        return False
    else:
        return True

flag=1
while(True):

    if(flag==1):

        string=from_network_layer()
        to_physical_layer(string)
        last_data=string

    else:
        to_physical_layer(last_data)

    boolean=wait_for_event()

    if(boolean):
        print("lost frame..send again")
        flag=0
        last_data=string
    else:
        flag=1
        print("frame received")

    if(string=="over"):
        break

c.close()


	

