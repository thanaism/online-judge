n, w = map(int, input().split())
s, t = [], []
for _ in range(n):
    si, ti, pi = map(int, input().split())
    s.append([si, pi])
    t.append([ti, pi])
s.sort()
t.sort()
MAX_LEN = t[-1][0] - s[0][0] + 1
plus = [0] * MAX_LEN
minus = [0] * MAX_LEN
pl = mi = 0
for i in range(1, n):
    pl += s[i - 1][1]
    mi -= t[i - 1][1]
    for j in range(s[i - 1][0], s[i][0]):
        plus[j] = pl
    for j in range(t[i - 1][0], t[i][0]):
        minus[j] = mi
for i in range(s[-1][0], t[-1][0]):
    plus[i] = pl + s[-1][1]
flg = True
for i in range(s[0][0], t[-1][0]):
    if plus[i] + minus[i] > w:
        flg = False
print("Yes" if flg else "No")
