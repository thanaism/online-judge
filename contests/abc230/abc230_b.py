s = input()
t = "oxx" * 20
ans = "No"
for i in range(len(t)):
    ok = True
    for j in range(len(s)):
        if i + j >= 60 or s[j] != t[i + j]:
            ok = False
            break
    if ok:
        ans = "Yes"
print(ans)
