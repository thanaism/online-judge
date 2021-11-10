n, k = map(int, input().split())
l = set(range(1, n + 1))
for _ in range(k):
    _ = input()
    l -= set([*map(int, input().split())])
print(len(l))
