n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
ans = []
for i in range(a - q, a - p + 1):
    buf = []
    for j in range(b - s, b - r + 1):
        if abs(i) == abs(j):
            buf.append("#")
        else:
            buf.append(".")
    ans.append(buf[::-1])

for line in ans[::-1]:
    print("".join(line))
