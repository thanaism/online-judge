n, q = map(int, input().split())
lr = []
for _ in range(q):
    l, r = map(int, input().split())
    lr.append((l - 1, r - 1))

rev = [0] * n
for l, r in lr:
    rev[l] += 1
    if r + 1 < n:
        rev[r + 1] -= 1

for i in range(1, n):
    rev[i] += rev[i - 1]

ans = ""
for i in rev:
    if i & 1:
        ans += "1"
    else:
        ans += "0"

print(ans)
