n, k = map(int, input().split())
p = [*map(int, input().split())]
print(sum(sorted(p)[:k]))
