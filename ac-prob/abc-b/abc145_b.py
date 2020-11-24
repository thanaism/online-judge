n=int(input())
s=input()
ans='Yes'
if n&1:ans='No'
if s[:n//2]!=s[n//2:]:ans='No'
print(ans)