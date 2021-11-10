n, m = map(int, input().split())
h = sorted(list(map(int, input().split())))
w = sorted(list(map(int, input().split())))
diff = []
max_v = 0
max_i = None
for i in range(1, len(h)):
    buf = h[i] - h[i - 1]
    max_v = max(max_v, buf)
    if max_v == buf:
        max_i = i
    diff.append(h[i] - h[i - 1])
if len(range(max_i)) % 2 == 0:
    max(h[i:])
