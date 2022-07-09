from itertools import groupby


s, t = input(), input()

gs = [(k, list(v)) for k, v in groupby(s)]
gt = [(k, list(v)) for k, v in groupby(t)]
n, m = len(gs), len(gt)

if n != m:
    print("No")
    exit()

for a, b in zip(gs, gt):
    la, lb = len(a[1]), len(b[1])
    if a[0] != b[0] or (la < 2 and lb >= 2) or la > lb:
        print("No")
        exit()

print("Yes")
