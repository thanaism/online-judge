n, x = map(int, input().split())
a = [*map(int, input().split())]

know = [0] * n
know[x - 1] = 1

while True:
    nxt = a[x - 1]
    if know[nxt - 1] == 0:
        know[nxt - 1] = 1
        x = a[x - 1]
    else:
        break

print(sum(know))
