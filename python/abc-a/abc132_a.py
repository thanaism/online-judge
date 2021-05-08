s=input()
t=set(s)
ans='Yes'
if len(t)!=2:
    ans='No'
elif s.count(s[0])!=2:
    ans='No'
print(ans)