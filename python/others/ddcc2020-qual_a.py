x, y = map(int, input().split())
if x == y == 1:
    ans = 1000000
else:
    s = [300000, 200000, 100000]
    for _ in range(300):
        s.append(0)
    ans = s[x - 1] + s[y - 1]
print(ans)
