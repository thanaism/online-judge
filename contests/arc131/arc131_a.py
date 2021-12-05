a = int(input())
b = int(input())
ans = str(a) + "0"
if b & 1 == 1:
    ans += str(b // 2) + "5"
else:
    ans += str(b // 2)

ans = int(ans)

# assert ans < 10 ** 18
# assert str(ans).count(str(a)) > 0
# assert str(ans * 2).count(str(b)) > 0

print(ans)
