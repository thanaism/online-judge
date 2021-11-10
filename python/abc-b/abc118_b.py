n, m = map(int, input().split())
ans = set(range(1, m + 1))
for _ in range(n):
    _, *a = map(int, input().split())
    ans &= set(a)
print(len(ans))
