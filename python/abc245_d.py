n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

import numpy as np

pa = np.poly1d(list(reversed(a)))
pc = np.poly1d(list(reversed(c)))
pb = pc / pa

print(*reversed(list(map(int, pb[0].c))))
