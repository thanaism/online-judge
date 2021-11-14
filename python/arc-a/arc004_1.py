from math import sqrt

n = int(input())
points = [tuple(map(float, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        ans = max(ans, sqrt(dx ** 2 + dy ** 2))

print(ans)
