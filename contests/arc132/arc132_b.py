n = int(input())
p = [*map(int, input().split())]

ans = 1 << 60
for i in range(n):
    j = (i + 1 + n) % n

    # 降順
    if p[i] == 1 and p[j] == n:
        # 反転してからn-i-1回動かす
        ans = min(ans, n - i)
        # i+1回動かしてから反転
        ans = min(ans, i + 2)

    # 昇順
    if p[i] == n and p[j] == 1:
        # j回動かす
        ans = min(ans, j)
        # 反転してからn-j回動かして再度反転
        ans = min(ans, n - j + 2)

print(ans)
