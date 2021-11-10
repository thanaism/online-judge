n, m = map(int, input().split())
a = [*map(int, input().split())]
print(max(-1, n - sum(a)))
