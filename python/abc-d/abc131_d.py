n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[1])

ans = "Yes"
now = 0

for a, b in ab:
    now += a
    if now > b:
        ans = "No"

print(ans)
