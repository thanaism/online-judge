q, h, s, d = map(int, input().split())
n = int(input())

min_d = min(8 * q, 4 * h, 2 * s, d)
min_s = min(4 * q, 2 * h, s)
min_h = min(2 * q, h)

n *= 4
n_d = n // 8
n %= 8
n_s = n // 4
n %= 4
n_h = n // 2
n %= 2

print(min_d * n_d + min_s * n_s + min_h * n_h + q * n)
