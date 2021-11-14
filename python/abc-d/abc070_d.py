from collections import defaultdict
from heapq import heappush, heappop


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


n = int(input())

dij = Dijkstra(n)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    dij.add(a - 1, b - 1, c)
    dij.add(b - 1, a - 1, c)

q, k = map(int, input().split())
dist = dij.calc(k - 1)
for _ in range(q):
    x, y = map(int, input().split())
    print(dist[x - 1] + dist[y - 1])
