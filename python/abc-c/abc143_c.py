n=int(input())
s=input()
ans=s[0]
for i in s:
    if i!=ans[-1]:
        ans+=i
print(len(ans))