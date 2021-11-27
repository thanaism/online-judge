from collections import defaultdict

int1 = lambda x: int(x) - 1

n, m = map(int, input().split())

edges = defaultdict(list)
for _ in range(m):
    a, b = map(int1, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in edges.keys():
    edges[i].sort(reverse=True)

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


uf = DSU(n)
con = 0
ans = [0]
for i in range(n - 1, 0, -1):
    con += 1
    for j in edges[i]:
        if j < i:
            break
        if not uf.connected(i, j):
            con -= 1
            uf.merge(i, j)
    ans.append(con)


for i in ans[::-1]:
    print(i)
