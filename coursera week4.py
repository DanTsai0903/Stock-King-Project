c=int(input()) #單位進貨成本
r=int(input()) #單位零售價格$$$
n=int(input()) #需求的可能個數
q=int(input()) #訂貨量
p=[]
for i in range(n+1):
	p.append(float(input()))
	
total1=0
total2=0

for a in range(1,q+1):
	income1=0
	income1=income1+a*r
	exp1=0
	exp1=income1*p[a]
	total1+=exp1
	
for b in range(q+1,n+1):
	income2=0
	income2=income2+q*r
	exp2=0
	exp2=income2*p[b]
	total2+=exp2
	
answer=int(total1+total2)-c*q


print(answer)