from collections import defaultdict

s = input()
k = int(input())
n = len(s)

fix = lambda: defaultdict(fix)
dp = defaultdict(fix)

dp[0][0][0] = (s, 1)

for _ in range(n):
    new_dp = defaultdict(fix)
    for x, d1 in dp.items():
        for e, d2 in d1.items():
            for y, (t, v) in d2.items():
                for c in "KEY":
                    if c in t:
                        i = t.index(c)
                        nx = x + i
                        ne = e + (c == "E")
                        ny = y + (c == "Y")
                        if ny in new_dp[nx][ne]:
                            new_dp[nx][ne][ny] = (
                                new_dp[nx][ne][ny][0],
                                new_dp[nx][ne][ny][1] + v,
                            )
                        else:
                            new_dp[nx][ne][ny] = (t[:i] + t[i + 1 :], v)
    dp = new_dp

ans = 0
for x, d1 in dp.items():
    if x > k:
        continue
    for e, d2 in d1.items():
        for y, (t, v) in d2.items():
            ans += v

print(ans)
