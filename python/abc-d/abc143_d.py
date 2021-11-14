n = int(input())
l = [*map(int, input().split())] + [0, 1 << 60]
l.sort()


def binary_search(ok, ng, arr, func):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if func(arr[mid]):
            ok = mid
        else:
            ng = mid
    return ok


ans = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        a, b = l[i], l[j]
        lower = lambda x: max(a - b, b - a) < x
        upper = lambda x: x < a + b
        min_c = max(j + 1, binary_search(n + 1, 0, l, lower))
        max_c = binary_search(0, n + 1, l, upper)
        ans += max(0, max_c - min_c + 1)
        if min_c <= i <= max_c:
            ans -= 1
        if min_c <= j <= max_c:
            ans -= 1

print(ans)
