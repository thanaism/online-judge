n,m=map(int,input().split())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
c=[]
for i in range(1,1001):
    if (i in a)^(i in b):
            c.append(i)
print(' '.join(map(str,c)))