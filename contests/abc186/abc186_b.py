h, w = map(int, input().split())
a = []
c = 100
for _ in range(h):
    b = [*map(int, input().split())]
    c = min(min(b), c)
    a.append(b)
ans = 0
for i in a:
    for j in i:
        ans += j - c
print(ans)
