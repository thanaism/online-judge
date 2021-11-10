n = int(input())
p = [*map(int, input().split())]
q = [0] * n
for i in range(n):
    q[p[i] - 1] = i + 1
print(*q)
