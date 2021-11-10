p = [*map(int, input().split())]
l = []
for i in p:
    l.append(chr(ord("a") + i - 1))
print("".join(l))
