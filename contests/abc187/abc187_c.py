n = int(input())
S = []
from collections import defaultdict

on = defaultdict(int)
off = defaultdict(int)
for _ in range(n):
    s = input()
    if s[0] == "!":
        s = s[1::]
        on[s] += 1
    else:
        off[s] += 1
    S.append(s)
ans = "satisfiable"
for i in S:
    if on[i] > 0 and off[i] > 0:
        ans = i
        break
print(ans)
