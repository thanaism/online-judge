import sys
from functools import lru_cache

sys.setrecursionlimit(1000000000)
a, n = map(int, input().split())
INF = 1 << 60


@lru_cache(maxsize=None)
def calc(n, ans):
    if n == 1:
        return ans
    buf = set()
    s = str(n)
    for i in range(len(s)):
        if s[i] == "0":
            break
        m = int(s[i:] + s[:i])
        if m % a == 0:
            buf.add((m // a, ans + i + 1))
    ret = INF
    for i in buf:
        ret = min(ret, calc(*i))
    return ret


ans = calc(n, 0)
if ans == INF:
    print(-1)
else:
    print(ans)
