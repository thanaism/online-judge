n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())
d = {"r": p, "s": r, "p": s}
nxt = {"r": "s", "s": "p", "p": "r"}

ans = 0
for i in range(n):
    now = t[i]
    ans += d[now]
    if i - k >= 0:
        pre = t[i - k]
        if now == pre:
            ans -= d[now]
            t[i] = nxt[t[i + k]] if i + k < n else nxt[t[i]]

print(ans)
