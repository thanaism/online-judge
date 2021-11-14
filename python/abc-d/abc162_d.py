n = int(input())
s = input()

r = [0] * n
g = [0] * n
b = [0] * n

for i in range(n):
    if s[i] == "R":
        r[i] = 1
    if s[i] == "G":
        g[i] = 1
    if s[i] == "B":
        b[i] = 1

for i in range(1, n):
    r[i] += r[i - 1]
    g[i] += g[i - 1]
    b[i] += b[i - 1]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            continue
        if j + 1 >= n:
            continue
        color = list({"R", "G", "B"} - {s[i], s[j]})[0]
        if color == "R":
            ans += r[-1] - r[j]
        if color == "G":
            ans += g[-1] - g[j]
        if color == "B":
            ans += b[-1] - b[j]
        k = 2 * j - i
        if k < n:
            if s[k] == color:
                ans -= 1

print(ans)
