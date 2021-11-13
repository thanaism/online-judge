class Dijkstra:
    def __init__(self, size):
        self.edges = defaultdict(list)
        self.size = size  # number of nodes

    def add(self, a, b, cost):
        self.edges[a].append((b, cost))

    def calc(self, start):
        dist = [1 << 60] * self.size
        dist[start] = 0
        q = []
        heappush(q, (0, start))
        while q:
            pre_cost, pre_index = heappop(q)
            for nxt_index, nxt_cost in self.edges[pre_index]:
                cost = pre_cost + nxt_cost
                if cost < dist[nxt_index]:
                    heappush(q, (cost, nxt_index))
                    dist[nxt_index] = cost
        return dist


from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, input().split())
dij = Dijkstra(n)
for _ in range(m):
    a, b, t = map(int, input().split())
    dij.add(a - 1, b - 1, t)
    dij.add(b - 1, a - 1, t)

ans = 1 << 60
for i in range(n):
    ans = min(ans, max(dij.calc(i)))

print(ans)
