n = int(input())
a = sorted([*map(int, input().split())])
b = sorted([*map(int, input().split())] + [0, 10 ** 10])
c = sorted([*map(int, input().split())] + [0, 10 ** 10])


def binary_search(ok, ng, arr, criteria):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if arr[mid] > criteria:
            ok = mid
        else:
            ng = mid
    return ok


cnt_b = [0] * (n + 2)
for i in range(1, n + 1):
    j = binary_search(n + 1, 0, c, b[i])
    cnt_b[i] = n - j + 1
for i in range(n + 1, 1, -1):
    cnt_b[i - 1] += cnt_b[i]

ans = 0
for i in range(n):
    j = binary_search(n + 1, 0, b, a[i])
    ans += cnt_b[j]
print(ans)
