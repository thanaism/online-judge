n = input()
a = [*map(int, input().split())]
print(sum(map(abs, a)))
print(sum(map(lambda x: x * x, a)) ** 0.5)
print(max(map(abs, a)))
