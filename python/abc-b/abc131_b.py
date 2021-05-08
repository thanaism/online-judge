n,l=map(int,input().split())
t=[]
for i in range(n):
    t.append(l+i)
t.sort(key=lambda x:abs(x))
print(sum(t[1:]))