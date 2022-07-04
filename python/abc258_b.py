n = int(input())
grid = [input() for _ in range(n)]

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(8):
            total = ""
            for m in range(n):
                ni = i + di[k] * m
                nj = j + dj[k] * m
                total += grid[ni % n][nj % n]
            ans = max(ans, int(total))

print(ans)
