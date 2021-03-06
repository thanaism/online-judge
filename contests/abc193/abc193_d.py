k=int(input())
s=input()
t=input()
sl=[0]*9
tl=[0]*9
ul=[k]*9
for i in range(4):
    sl[int(s[i])-1]+=1
    tl[int(t[i])-1]+=1
    ul[int(s[i])-1]-=1
    ul[int(t[i])-1]-=1
# print(sl,tl,ul)
ans=0
for i in range(9):
    sp=0
    for si,sv in enumerate(sl):
        if si==i:sv+=1
        sp+=(si+1)*(10**sv)
    sq=ul[i]/(9*k-8)
    for j in range(9):
        tp=0
        for ti,tv in enumerate(tl):
            if ti==j:tv+=1
            tp+=(ti+1)*(10**tv)
        tq=(ul[j] if j!=i else max(ul[j]-1,0))/(9*k-9)
        if sp>tp:
            # print(i,j)
            ans+=sq*tq
print(ans)