from collections import defaultdict, deque

n, m = map(int, input().split())
edges = defaultdict(list)
for i in range(m):
    u, v, l = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((l, v))
    edges[v].append((l, u))

# Warshall-Floyed Alogrithm
# n: vertex_count
# cost[i][j]: cost from i to j
INF = 1 << 60
cost = [[INF] * n for _ in range(n)]
# --- INPUT COST OF EDGES HERE---
for i in edges:
    for c, j in edges[i]:
        if i != 0 and j != 0:
            cost[i][j] = c
# --- INPUT COST OF EDGES HERE---
for k in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

ans = INF
length = len(edges[0])
for i in range(length):
    for j in range(i + 1, length):
        cost_i = edges[0][i][0]
        cost_j = edges[0][j][0]
        ind_i = edges[0][i][1]
        ind_j = edges[0][j][1]
        ans = min(ans, cost_i + cost_j + cost[ind_i][ind_j])

print(-1 if ans == INF else ans)
