n=int(input())
h=[*map(int,input().split())]
ans=0
i=0
while i<n-1:
    j=i+1
    while j<n and h[j-1]>=h[j]:
        ans=max(ans,j-i)
        j+=1
    i=j
print(ans)