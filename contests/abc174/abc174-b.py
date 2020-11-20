from sys import stdin

N, D = stdin.readline().rstrip().split()
DD = int(D) ** 2
N = int(N)

CNT = 0

for i in range(N):
  X, Y = stdin.readline().rstrip().split()
  XX = int(X) ** 2
  YY = int(Y) ** 2
  ZZ = XX + YY
  if ZZ <= DD:
    CNT += 1
      
print(CNT)