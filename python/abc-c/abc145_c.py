n = int(input())
mat = []
for _ in range(n):
    mat.append([*map(int, input().split())])
from itertools import permutations

ans = 0
for i in permutations(range(n)):
    for j in range(n - 1):
        a, b = i[j + 1], i[j]
        dx = mat[a][0] - mat[b][0]
        dy = mat[a][1] - mat[b][1]
        ans += (dx * dx + dy * dy) ** 0.5


def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


print(ans / fact(n))
