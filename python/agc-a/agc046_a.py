x=int(input())
a=x
ans=1
while a%360!=0:
    a+=x
    ans+=1
print(ans)