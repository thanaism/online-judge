x = int(input())

d = {}
for i in range(-1000, 1001):
    d[i * i * i * i * i] = i

for p in d:
    if x + p in d:
        print(d[x + p], d[p])
        exit()
