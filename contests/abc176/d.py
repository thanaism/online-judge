from collections import deque

(h, w), (ch, cw), (dh, dw) = eval("map(int,input().split())," * 3)
ss = [list(map(str, input())) for _ in range(h)]
q = deque([(ch - 1, cw - 1, 0)])
while q:
    j, i, c = q.popleft()
    if ss[j][i] == ".":
        ss[j][i] = c
    for s in range(-2, 3):
        for t in range(-2, 3):
            if 0 <= j + t < h and 0 <= i + s < w and ss[j + t][i + s] == ".":
                if abs(t) + abs(s) == 1:
                    q.appendleft((j + t, i + s, c))
                elif abs(t) + abs(s) >= 2:
                    q.append((j + t, i + s, c + 1))
if ss[dh - 1][dw - 1] == ".":
    print(-1)
else:
    print(ss[dh - 1][dw - 1])
