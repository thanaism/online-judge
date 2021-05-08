n=int(input())
w=[*map(int,input().split())]
ans=1<<30
s1=0
total=sum(w)
for i in w:
   s1+=i
   ans=min(abs(total-s1-s1),ans)
print(ans) 