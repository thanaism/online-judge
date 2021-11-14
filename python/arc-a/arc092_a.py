n = int(input())
ab = [[*map(int, input().split())] + [i] for i in range(n)]
cd = [[*map(int, input().split())] + [i] for i in range(n)]

ab.sort(key=lambda x: -x[1])
cd.sort()

used = set()
ans = 0
for c, d, i in cd:
    for a, b, j in ab:
        if c <= a or d <= b or j in used:
            continue
        used.add(j)
        ans += 1
        break
print(ans)
