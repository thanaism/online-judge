"""
f=input;a=int(f());b,c=map(int,f().split());s=f();print(a+b+c,s)
print(sum(map(int,(l:=' '.join([*open(0)]).split())[0:3])),l[3])
print(sum(map(int,((l:=[*open(0)])[0]+l[1]).split())),l[2])
*l,=open(0);print(sum(map(int,(l[0]+l[1]).split())),l[2])
*a,s=open(0).read().split();print(sum(map(int,a)),s)
f=input;print(sum(map(int,[f(),*f().split()])),f())
x,y,z=open(0);print(sum(map(int,[x,*y.split()])),z)
a,b,s=open(0);print(sum(map(int,(a+b).split())),s)
"""

i=input;print(sum(map(int,[i()]+i().split())),i())
