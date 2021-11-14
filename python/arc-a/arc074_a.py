h, w = map(int, input().split())

ans = h * w
for h1 in range(1, h):
    h2 = (h - h1) // 2
    h3 = h - h1 - h2
    smax = max(h1, h2, h3) * w
    smin = min(h1, h2, h3) * w
    ans = min(ans, smax - smin)
    w1 = w // 2
    w2 = w - w1
    smax = max(h1 * w, (h - h1) * w1, (h - h1) * w2)
    smin = min(h1 * w, (h - h1) * w1, (h - h1) * w2)
    ans = min(ans, smax - smin)

for w1 in range(1, w):
    w2 = (w - w1) // 2
    w3 = w - w1 - w2
    smax = max(w1, w2, w3) * h
    smin = min(w1, w2, w3) * h
    ans = min(ans, smax - smin)
    h1 = h // 2
    h2 = h - h1
    smax = max(w1 * h, (w - w1) * h1, (w - w1) * h2)
    smin = min(w1 * h, (w - w1) * h1, (w - w1) * h2)
    ans = min(ans, smax - smin)

print(ans)
