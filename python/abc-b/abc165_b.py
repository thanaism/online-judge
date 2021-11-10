x = int(input())
a = 100
ans = 0
while a < x:
    ans += 1
    a *= 101
    a //= 100
print(ans)
