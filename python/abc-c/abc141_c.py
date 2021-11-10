n, k, q = map(int, input().split())
a = [int(input()) - 1 for _ in range(q)]
from collections import defaultdict

dd = defaultdict(int)
for i in a:
    dd[i] += 1
for i in range(n):
    print("Yes" if k + dd[i] - q > 0 else "No")
