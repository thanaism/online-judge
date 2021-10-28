# Disjoint Set Union library
class DSU:
    def __init__(self, n):
        self.n = n
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

    def members(self):
        members = {}
        for i in range(self.n):
            key = self.root(i)
            if key in members:
                members[key].append(i)
            else:
                members[key] = [i]
        return members.values()


n, m = map(int, input().split())
p = [*map(lambda x: int(x) - 1, input().split())]
dsu = DSU(n)
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    dsu.merge(x, y)

members = dsu.members()
unmatch = set()
for val in members:
    indices = set(val)
    digits = set()
    for i in val:
        digits.add(p[i])
    unmatch |= indices - digits

print(n - len(unmatch))
