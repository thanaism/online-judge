s=input()
n=len(s)//2+1
ans=0
for i,j in zip(s[:n],s[-1:-n:-1]):
    if i!=j:ans+=1
print(ans)