a,b=map(int,input().split())
s=input()
ans='Yes'
if len(s)!=a+b+1:
    ans='No'
else:
    for i in s[:a]:
        if i  not in map(str,range(10)):
            ans='No'
    if s[a]!='-':
        ans='No'
    for i in s[a+1:]:
        if i  not in map(str,range(10)):
            ans='No'
print(ans)