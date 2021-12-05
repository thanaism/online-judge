n, d = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(n)]
lr.sort(key=lambda x: x[1])
ans = 0
now = -(1 << 60)
for l, r in lr:
    if now + d - 1 < l:
        ans += 1
        now = r
print(ans)
