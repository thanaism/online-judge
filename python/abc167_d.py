n, k = map(int, input().split())
a = [*map(int, input().split())]

x = 1
s = set()
c = 0
while x not in s:
    s.add(x)
    last_town = x
    x = a[x - 1]
    c += 1

loop = 1
while x != last_town:
    x = a[x - 1]
    loop += 1

ans = None
if k < c:
    x = 1
    while k:
        k -= 1
        ans = x
        x = a[x - 1]
    print(ans)
else:
    k -= c
    k = k % loop
    x = last_town
    while k:
        k -= 1
        ans = x
        x = a[x - 1]
    print(ans)
