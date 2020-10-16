"""サンプルケースTLE
これだとcを呼び出すたびにO(N)
cをO(N)で作って呼び出しはO(1)にする

n = int(input())

c = lambda i, j: len(
    [
        k
        for k in range(1, n+1)
        if (
            str(k)[0] == str(i) and str(k)[-1] == str(j)
        )
    ]
)

count = 0
for i in range(10):
    for j in range(10):
          count += c(i, j) * c(j, i)
print(count)
"""

n = int(input())
c = [[0] * 10 for _ in range(10)]
for k in range(1, n + 1):
    c[int(str(k)[0])][int(str(k)[-1])] += 1

count = 0
for i in range(10):
    for j in range(10):
        count += c[i][j] * c[j][i]
print(count)