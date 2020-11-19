n=int(input())
a=[*map(int,input().split())]
ans=0
for i,v in enumerate(a):
    if -~i&1 and v&1:
        ans+=1 
print(ans)