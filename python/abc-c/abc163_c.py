n = int(input())
a = [*map(int, input().split())]
ans = [0] * n
for i in a:
    ans[i - 1] += 1
for i in ans:
    print(i)
