n,m=map(int,input().split())
l=['']*n
ok=True
for _ in range(m):
    s,c=input().split()
    i=int(s)-1
    if l[i]!='':
        if l[i]==c:continue
        ok=False
        break
    else:
        l[i]=c
if ok:
    ans=''
    zero=True
    if n==1:zero=False
    for i in l:
        if i:
            ans+=i
            zero=False
        elif zero:
            ans+='1'
            zero=False
        else:    
            ans+='0'
    if n>1 and int(ans)==0:
        ans=-1
else:
    ans=-1
print(ans)