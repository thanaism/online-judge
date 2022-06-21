h, w = map(int, input().split())
r, c = map(int, input().split())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

ans = 0
for k in range(4):
    i = r + di[k]
    j = c + dj[k]
    if 1 <= i <= h and 1 <= j <= w:
        ans += 1

print(ans)
