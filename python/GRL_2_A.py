# Kruskal's algorithm library
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


class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost


class Kruskal:
    def __init__(self, vertex_count, edges):
        self.edges = edges
        self.vertex_count = vertex_count

    def calc(self):
        self.edges.sort(key=lambda e: e.cost)
        dsu = DSU(self.vertex_count)
        total = 0
        for e in self.edges:
            if not dsu.connected(e.u, e.v):
                dsu.merge(e.u, e.v)
                total += e.cost
        return total


# Kruskal's algorithm library

v, e = map(int, input().split())
edges = []
for _ in range(e):
    s, t, w = map(int, input().split())
    edges.append(Edge(s, t, w))
krs = Kruskal(v, edges)
print(krs.calc())
