e=set([*map(int,input().split())])
b=int(input())
l=set([*map(int,input().split())])
d=l-e
cnt=6-len(d)
if cnt==5:
    ans=3
    if b in d:ans=2
elif cnt==6:
    ans=1
elif cnt==4:
    ans=4
elif cnt==3:
    ans=5
else:
    ans=0
print(ans)

