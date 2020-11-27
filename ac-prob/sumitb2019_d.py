n=int(input())
s=input()
ans=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            f1=f2=f3=False
            for l in s:
                if f1==False and l==str(i):
                    f1=True
                    continue
                if f2==False and f1 and l==str(j):
                    f2=True
                    continue
                if f3==False and f1 and f2 and l==str(k):
                    f3=True
                    continue
            if f1 and f2 and f3:ans+=1
print(ans)