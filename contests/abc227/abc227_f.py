from heapq import *

h, w, k = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(h)]

heaps = [[[] for _ in range(w)] for _ in range(h)]
cost = [[1 << 60] * w for _ in range(h)]
heappush(heaps[0][0], a[0][0])
for i in range(h):
    for j in range(w):
        if i == j == 0:
            continue
        if i - 1 >= 0:
            nxt = []
            heappush(nxt, -a[i][j])
            pre = heaps[i - 1][j].copy()
            while pre:
                heappush(nxt, -heappop(pre))
            buf1 = 0
            nxt1 = []
            m = 0
            while nxt:
                tmp = -heappop(nxt)
                heappush(nxt1, tmp)
                if m < k:
                    buf1 += tmp
                m += 1
        if j - 1 >= 0:
            nxt = []
            heappush(nxt, -a[i][j])
            pre = heaps[i][j - 1].copy()
            while pre:
                heappush(nxt, -heappop(pre))
            buf2 = 0
            nxt2 = []
            m = 0
            while nxt:
                tmp = -heappop(nxt)
                heappush(nxt2, tmp)
                if m < k:
                    buf2 += tmp
                m += 1
        if i - 1 >= 0 and j - 1 >= 0:
            if buf1 < buf2:
                heaps[i][j] = nxt1.copy()
                cost[i][j] = min(cost[i][j], buf1)
            else:
                heaps[i][j] = nxt2.copy()
                cost[i][j] = min(cost[i][j], buf2)
        elif i - 1 < 0:
            heaps[i][j] = nxt2.copy()
            cost[i][j] = min(cost[i][j], buf2)
        elif j - 1 < 0:
            heaps[i][j] = nxt1.copy()
            cost[i][j] = min(cost[i][j], buf1)

print(cost[h - 1][w - 1])
