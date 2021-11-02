from collections import deque

n, q = map(int, input().split())
front = [-1] * (n + 1)
back = [-1] * (n + 1)
for _ in range(q):
    query = input().split()
    if len(query) < 3:
        _, x = map(int, query)
        d = deque()
        d.append(x)
        i = x
        while front[i] != -1:
            d.appendleft(front[i])
            i = front[i]
        i = x
        while back[i] != -1:
            d.append(back[i])
            i = back[i]
        print(len(d), *d)
        continue
    c, x, y = map(int, query)
    if c == 1:
        back[x] = y
        front[y] = x
    else:
        back[x] = -1
        front[y] = -1
