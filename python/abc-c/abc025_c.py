b = [[*map(int, input().split())] for _ in range(2)]
c = [[*map(int, input().split())] for _ in range(3)]


def calc(grid):
    x = y = 0
    for i in range(3):
        for j in range(3):
            if i + 1 < 3:
                if grid[i][j] == grid[i + 1][j]:
                    x += b[i][j]
                else:
                    y += b[i][j]
            if j + 1 < 3:
                if grid[i][j] == grid[i][j + 1]:
                    x += c[i][j]
                else:
                    y += c[i][j]
    return x - y


def game(n, grid):
    if n == 9:
        return calc(grid)
    INF = 1 << 60
    score = INF if n & 1 else -INF
    for i in range(3):
        for j in range(3):
            if grid[i][j] == -1:
                if n & 1:
                    grid[i][j] = 1
                    score = min(score, game(n + 1, grid))
                else:
                    grid[i][j] = 0
                    score = max(score, game(n + 1, grid))
                grid[i][j] = -1
    return score


grid = [[-1] * 3 for _ in range(3)]
score = game(0, grid)
total = 0
for line in b:
    total += sum(line)
for line in c:
    total += sum(line)
x = (score + total) // 2
y = total - x
print(x)
print(y)
