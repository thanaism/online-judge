"""l=int(input())
ans=0
for i in range(l):
    for j in range(l):
        if l-i-j>0:
            ans=max((l-i-j)*i*j,ans)
print(ans)"""

l = int(input())
print((l / 3) ** 3)
