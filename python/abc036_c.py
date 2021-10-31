n = int(input())
a = [int(input()) for _ in range(n)]

l = sorted(list(set(a)))
d = {}
i = 0
for x in l:
    d[x] = i
    i += 1

for i in a:
    print(d[i])
