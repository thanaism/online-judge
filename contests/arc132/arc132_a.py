n = int(input())
r = [*map(int, input().split())]
c = [*map(int, input().split())]

q = int(input())

ans = ""
for _ in range(q):
    i, j = map(lambda x: int(x) - 1, input().split())
    if n - r[i] + 1 <= c[j] <= n:
        ans += "#"
    else:
        ans += "."

print(ans)
