n = int(input())
l = sorted([*map(int, input().split())])
print(sum(l[::2]))
