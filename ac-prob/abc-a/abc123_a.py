*l,k=map(int,open(0).read().split())
ans='Yay!'
for i in range(4):
    for j in range(i+1,5):
        if abs(l[i]-l[j])>k:ans=':('
print(ans)