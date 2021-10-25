n = int(input())
f = [[*map(int, input().split())] for _ in range(n)]
p = [[*map(int, input().split())] for _ in range(n)]

INF = 1 << 60
ans = -INF
for bit in range(1, 1 << 10):
    cnt = [0] * n
    point = [0] * n
    for store in range(n):
        for i in range(10):
            if bit >> i & 1 and f[store][i]:
                cnt[store] += 1
        point[store] = p[store][cnt[store]]
    ans = max(ans, sum(point))

print(ans)
