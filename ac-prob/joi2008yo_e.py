r,c=map(int,input().split())
rc=[]
for _ in range(r):
    rc.append([*map(int,input().split())])
for i in ranga(1<<r):
    b=bin(i)[2::].zfill(r)
    
