n,x=map(int,input().split())
a=[*map(int,input().split())]
ans=[]
for i in a:
    if i!=x:ans.append(str(i))
print(' '.join(ans))