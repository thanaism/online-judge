from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    s = input()
    d[s] += 1
d = sorted(d.items(), key=lambda x: -x[1])
print(d[0][0])
