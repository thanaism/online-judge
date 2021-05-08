s=input()
ans='Good'
for i in range(1,4):
    if s[i-1]==s[i]:
        ans='Bad'
print(ans)