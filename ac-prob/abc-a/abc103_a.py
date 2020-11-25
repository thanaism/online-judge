a=[*map(int,input().split())]
d=[]
for i in range(2):
    for j in range(i+1,3):
        d.append(abs(a[i]-a[j]))
d.sort()
print(sum(d[:2]))