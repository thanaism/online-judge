from heapq import *

INF = 1 << 60


def dijkstra(x, si, sj):
    hq = []
    heappush(hq, (0, si, sj))
    cost = [[INF] * w for _ in range(h)]
    cost[si][sj] = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while hq:
        c, i, j = heappop(hq)
        if c > cost[i][j]:
            continue
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            tmp = cost[i][j] + (x if s[ni][nj] == "#" else 1)
            if tmp < cost[ni][nj]:
                cost[ni][nj] = tmp
                heappush(hq, (tmp, ni, nj))
    return cost


h, w, t = map(int, input().split())
s = []
for i in range(h):
    line = input()
    for j in range(w):
        if line[j] == "S":
            si, sj = i, j
        if line[j] == "G":
            gi, gj = i, j
    s.append(line)

ok = 1
ng = t
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if dijkstra(mid, si, sj)[gi][gj] <= t:
        ok = mid
    else:
        ng = mid

print(ok)
