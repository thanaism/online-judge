s, t, x = map(int, input().split())

on = [False] * 24
for i in range(24):
    u = (s + i) % 24
    if u == t:
        break
    on[u] = True

if on[x]:
    print("Yes")
else:
    print("No")
