n = int(input())
from collections import defaultdict

s = defaultdict(int)
t = set()
for _ in range(n):
    a = input()
    t |= {a}
    s[a] += 1
m = max(s.items(), key=lambda x: x[1])
for i in sorted(t):
    if s[i] == m[1]:
        print(i)
