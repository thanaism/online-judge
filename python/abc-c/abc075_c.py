# Disjoint Set Union library
class DSU:
    def __init__(self, n):
        self.parent = [-1] * n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if rx > ry:
            rx, ry = ry, rx
        self.parent[rx] += self.parent[ry]
        self.parent[ry] = rx

    def size(self, x):
        return -self.parent[self.root(x)]

    def connected(self, x, y):
        return self.root(x) == self.root(y)


# Disjoint Set Union library

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

ans = 0
for remove in range(m):
    dsu = DSU(n + 1)
    for i in range(m):
        if i == remove:
            continue
        a, b = edges[i]
        dsu.merge(a, b)
    if dsu.size(1) != n:
        ans += 1

print(ans)
