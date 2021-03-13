n=int(input())
m=(len(str(n))-1)//3
p=10**(m*3)
ans=0
for i in range(m):
    x=10**(i*3)
    y=10**((i+1)*3)
    ans+=(y-x)*i
print(ans+(n-p+1)*m)
