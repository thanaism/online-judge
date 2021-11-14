from collections import Counter

n = int(input())
a = [*map(int, input().split())]

ca = Counter(a)
sa = sorted(ca.items())
sa = [i for _, i in sa]
na = len(sa)

d = 0
for i in range(na):
    if sa[i] > 1:
        if sa[i] > 2:
            if sa[i] & 1:
                sa[i] = 1
            else:
                sa[i] = 2
        d += sa[i] - 1
        sa[i] = 1
        for j in range(na - 1, i, -1):
            if d == 0:
                break
            if sa[j] > 1:
                if sa[j] - 1 <= d:
                    d -= sa[j] - 1
                    sa[j] = 1
                else:
                    sa[j] -= d
                    d = 0
if d:
    print(na - d)
else:
    print(na)
