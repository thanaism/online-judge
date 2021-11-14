n = int(input())
c = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    c[a - 1] += 1
    c[b - 1] += 1
ok = False
for i in c:
    if i == n - 1:
        ok = True
if ok:
    print("Yes")
else:
    print("No")
