n = int(input())
a = [*map(int, input().split())]

xor = 0
for i in a:
    xor ^= i

if xor in a:
    ans = "Win"
elif n & 1:
    ans = "Win"
else:
    ans = "Lose"

print(ans)
