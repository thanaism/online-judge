n, k = map(int, input().split())
d = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = b
    else:
        d[a] += b

for key, val in sorted(d.items()):
    if k > val:
        k -= val
    else:
        print(key)
        break
