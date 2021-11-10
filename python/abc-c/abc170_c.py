x, n = map(int, input().split())
p = set([*map(int, input().split())])
q = sorted(set(range(-1, 102)) - p)
r = q[0]
for i in q:
    if abs(x - i) < abs(x - r):
        r = i
print(r)
