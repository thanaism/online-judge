n=int(input())
h=[*map(int,input().split())]
m=0
ans='Yes'
for i in h:
    m=max(m,i)
    if i<m-1:ans='No'
print(ans)