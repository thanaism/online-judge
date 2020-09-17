"""
a,b,c,x=map(int,open(0))
l=[]
for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      l+=500*i+100*j+50*k==x,
print(sum(l))

a,b,c,x=eval('int(input())+1,'*4);print(sum(10*i+2*j+k==x//50 for i in range(a)for j in range(b)for k in range(c)))
a,b,c,x=map(int,open(0));print(sum(500*i+100*j+50*k==x for i in range(a+1)for j in range(b+1)for k in range(c+1)))
a,b,c,x=map(int,open(0));print(sum(10*i+2*j+k==x/50 for i in range(a+1)for j in range(b+1)for k in range(c+1)))
a,b,c,x=eval('int(input())+1,'*4);print(sum(i//b*10+i%b*2+j==x//50for i in range(a*b)for j in range(c)))
a,b,c,x=eval('int(input())+1,'*4);print(sum(i//b*10+i%b*2+j==x/50for i in range(a*b)for j in range(c)))
a,b,c,x=map(int,open(0));print(sum(i//-~b*10+i%-~b*2+j==x/50for i in range(~a*~b)for j in range(c+1)))
"""

a,b,c,x=map(int,open(0));print(sum(-1<x/50-i//-~b*10-i%-~b*2<c+1for i in range(~a*~b)))
