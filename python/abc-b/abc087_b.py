a,b,c,x=map(int,open(0))
ans=0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 10*i+2*j+k==x//50:ans+=1
print(ans)