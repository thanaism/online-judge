a, b, c = map(int, input().split())
ans = []
for i in range(1, 128):
    if i % 3 == a and i % 5 == b and i % 7 == c:
        print(i)
