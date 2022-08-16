import socket,math,random
b = {}
def power_two(n): 
    return (math.ceil(math.log2(n)) == math.floor(math.log2(n))); 

def chk_bit(n):
    while n:
        b = n & (~n+1)
        yield b
        n ^= b

def hamming_code(x):
	templist = []

	for b in chk_bit(x):
		templist.append(b)
	
	b[x]=templist		

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))

s.listen(5)

connect,address = s.accept()


msg = connect.recv(1024)

m1 = list(msg)
m2 = list(msg)

st = ""

for i in range(len(m1)):
	if(power_two(i+1)==False):
		st+=m1[i]

st_list = list(st)

r = 0
while(len(st_list)+r+1<=pow(2,r)):
	r+=1

count = 0
in = 3

while((count<len(st_list))):
	if(power_two(in)==False):
		count+=1
		hamming_code(in)					
	in+=1

print(b)

temp = -1

ms = []

cnt = 0

for i in range(in):
	ms.append(temp)

for i in range(1,in):
	if(power_two(i)==False):
		ms[i]=st[cnt]
		cnt+=1

for i in range(1,in):
	tlist = []
	if(power_two(i)==True):
		for keys,values in b.items():
			if(i in b[keys]):
				tlist.append(ms[keys])

		count_ones=0		
		for j in range(len(tlist)):
			if(tlist[j]=='1'):
				count_ones+=1

		if(count_ones%2==0):
			ms[i]='0'
		else:
			ms[i]='1'		

string_to_be_send = ""
for i in range(1,len(ms)):
	string_to_be_send+=ms[i]

#Store Parity of initial string

parity_first = []
parity_second= []

for i in range(0,len(m2)):
	if(power_two(i+1)):
		parity_first.append(int(m2[i]))

for i in range(1,len(ms)+1):
	if(power_two(i)):
		parity_second.append(int(ms[i]))


parity_final = []

for i in range(len(parity_first)):
	x = parity_first[i]^parity_second[i]
	parity_final.append(x)


parity_final.reverse()

final_bit_string = ""

for i in range(len(parity_final)):
	final_bit_string+=str(parity_final[i])

position_to_be_corrected = int(final_bit_string,2)

print("error")
print(position_to_be_corrected)
if(m2[position_to_be_corrected-1]=='0'):
	m2[position_to_be_corrected-1]='1'
else:
	m2[position_to_be_corrected-1]='0'

print("After correction")
print(m2)

connect.close()
s.close()
