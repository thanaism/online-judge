x = input()
n = len(x)

# 文字列解
l = [int(c) for c in x]
for i in range(1, n):
    l[i] += l[i - 1]

up = 0
s = ""
for i in range(n - 1, -1, -1):
    d = l[i] + up
    up = d // 10
    s += str(d % 10)
if up > 0:
    s += str(up)
ans1 = s[::-1]

# 多倍長整数解
t = sum([int(c) for c in x])
x = int(x)
ans2 = str((10 * x - t) // 9)

if ans1 == ans2:
    print(ans2)
