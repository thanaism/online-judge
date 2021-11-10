n = int(input())
a = list(map(int, input().split()))
l = min(a)
u = max(a)
s = set(a)
# print(s)
t = list(s)
t.sort()
# print(t)
b = 0
for i in range(1, len(t)):
    if t[i] != t[i - 1]:
        b += t[i] - t[i - 1] - 1
print(b)
cnt = 1
for i in range(1, n):
    if a[i] == a[i - 1]:
        cnt *= 1
print(cnt)
ans = 1 << u
ans /= cnt
ans %= 10 ** 9 + 7
print(ans)
print((1 << (u - b)) % (10 ** 9 + 7))
diff = len(a) - len(t)
ans = 1 << (u - diff)
print(ans % (1000000007))
