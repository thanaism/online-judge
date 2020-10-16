# 制約が10^9なの見てなくてsum(range(n))とかやってTLEした。ダサい。

n = int(input())
print(n * (n - 1) // 2)
