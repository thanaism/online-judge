n=int(input())
a=[*map(int,input().split())]
ans=1
if 0 in a:
    print(0)
    exit()
for i in a:
    ans*=i
    if ans>10**18:
        ans=-1
        break
print(ans)