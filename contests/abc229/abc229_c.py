n, w = map(int, input().split())

pizza = []
for _ in range(n):
    a, b = map(int, input().split())
    pizza.append((a, b))

pizza.sort(reverse=True)

ans = 0
now = 0
for a, b in pizza:
    if now + b < w:
        now += b
        ans += a * b
    else:
        ans += a * (w - now)
        break
print(ans)
