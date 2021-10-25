s = input()
t = input()

ans = []
for i in range(len(s)):
    ok = True
    for j in range(len(t)):
        if not i+j<len(s):
            ok = False
            break
        if s[i+j] != t[j] and s[i+j] != '?':
            ok = False
    if ok:
        st = s[:i]+t+s[i+len(t):]
        ans.append(st.replace('?','a'))

if not ans:
    print('UNRESTORABLE')
else:
    ans.sort()
    print(ans[0])
