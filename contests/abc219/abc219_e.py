b=int(''.join(c for c in input()+input()+input()+input() if c!=' ')[::-1],2)
ex=[[0]*6 for _ in range(6)]
ans=0
for i in range(1<<16):
    if i&b!=b:continue
    p=[-1]*36
    def r(x):
        if p[x]<0:return x
        p[x]=r(p[x])
        return p[x]
    def u(x,y):
        x=r(x)
        y=r(y)
        if x==y:return
        if x>y:x,y=y,x
        p[x]+=p[y]
        p[y]=x
    def s(x):
        return -p[r(x)]
    t=0
    for j in range(4):
        for k in range(4):
            f=i>>j*4+k&1
            ex[-~j][-~k]=f
            if f:t=-~j*6-~k
    for j in range(6):
        for k in range(6):
            if -~j<6 and ex[j][k]==ex[-~j][k]:u(j*6+k,-~j*6+k)
            if -~k<6 and ex[j][k]==ex[j][-~k]:u(j*6+k,j*6-~k)
    ans+=s(t)+s(0)==36
print(ans)