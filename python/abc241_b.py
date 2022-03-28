n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = set()
for i in b:
    ok = False
    for j in range(n):
        if a[j] == i and j not in s:
            ok = True
            s.add(j)
            break
    if not ok:
        print("No")
        exit()
print("Yes")
