import socket,math,random

b = {}

def power_two(n): 
    return (math.ceil(math.log2(n)) == math.floor(math.log2(n))); 

def bn(n):
    while n:
        b = n & (~n+1)
        yield b
        n ^= b

def hamming_code(x):
	templist = []

	for b in bn(x):
		templist.append(b)
	
	b[x]=templist	



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

print("Enter bits to send")

msg = input()
d = list(msg)

r = 0
while(len(d)+r+1<=pow(2,r)):
	r+=1
cnt = 0
i_n = 3

while((cnt<len(d))):
	if(power_two(i_n)==False):
		cnt+=1
		hamming_code(i_n)					
	i_n+=1

print(b)

temp = '-1'

ms = []

ic = 0

for i in range(i_n):
	ms.append(temp)

for i in range(1,i_n):
	if(power_two(i)==False):
		ms[i]=msg[ic]
		ic+=1

for i in range(1,i_n):
	tlist = []
	if(power_two(i)==True):
		for keys,values in b.items():
			if(i in b[keys]):
				tlist.append(ms[keys])

		cnt_ones=0		
		for j in range(len(tlist)):
			if(tlist[j]=='1'):
				cnt_ones+=1

		if(cnt_ones%2==0):
			ms[i]='0'
		else:
			ms[i]='1'		


string_to_be_send = ""

print("here")
print(ms)
indices = []

for i in range(1,len(ms)+1):
	if(power_two(i)==False):
		indices.append(i)

random.shuffle(indices)

if(ms[indices[0]]=='1'):
	ms[indices[0]]='0'
else:
	ms[indices[0]]='1'

for i in range(1,len(ms)):
	string_to_be_send+=ms[i]

s.send(string_to_be_send)

