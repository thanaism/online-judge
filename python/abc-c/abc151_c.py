n, m = map(int, input().split())
ac = [0] * n
wa = [0] * n
for _ in range(m):
    p, s = input().split()
    p = int(p) - 1
    if s == "WA":
        if ac[p] == 0:
            wa[p] += 1
    else:
        ac[p] = 1
for i in range(n):
    if not ac[i]:
        wa[i] = 0
print(sum(ac), sum(wa))
