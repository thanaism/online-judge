"""
print(min([bin(int(i))[::-1].find('1') for i in [*open(0)][1].split()]))
print(min([len(bin((j:=int(i))&-j))-3 for i in [*open(0)][1].split()]))
print(min([len(bin(int(i)&-int(i)))-3 for i in [*open(0)][1].split()]))
a,b=open(0);print(min([len(bin(int(i)&-int(i)))-3 for i in b.split()]))
input();c=eval(input().replace(*' |'));print(len(bin(c&-c))-3)
a,b=open(0);print(len(bin((i:=eval(b.replace(*' |')))&-i))-3)
c=eval([*open(0)][1].replace(*' |'));print(len(bin(c&-c))-3)
"""

a,b=open(0);c=eval(b.replace(*' |'));print(len(bin(c&-c))-3)
