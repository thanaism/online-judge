n,k=map(int,input().split())
ans=n
for i in range(k):
    a=int(''.join(sorted(str(n))))
    b=int(''.join(sorted(str(n),reverse=True)))
    n=b-a
    ans=n
print(ans)