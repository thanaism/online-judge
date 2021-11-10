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

b = int("".join(c for c in input() + input() + input() + input() if c != " ")[::-1], 2)
ex = [[0] * 6 for _ in range(6)]
ans = 0
for i in range(1 << 16):
    if i & b != b:
        continue
    uft = DSU(36)
    t = 0
    for j in range(4):
        for k in range(4):
            f = i >> j * 4 + k & 1
            ex[-~j][-~k] = f
            if f:
                t = -~j * 6 - ~k
    for j in range(6):
        for k in range(6):
            if -~j < 6 and ex[j][k] == ex[-~j][k]:
                uft.merge(j * 6 + k, -~j * 6 + k)
            if -~k < 6 and ex[j][k] == ex[j][-~k]:
                uft.merge(j * 6 + k, j * 6 - ~k)
    ans += uft.size(t) + uft.size(0) == 36
print(ans)
