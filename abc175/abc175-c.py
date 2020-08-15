# 絶対値が最小になるように移動する
# 貪欲法である可能性を考える
# Xの正負で場合分けすればOKっぽい
# 15乗なので素直な実装では間に合わない

X, K, D = map(int, input().rstrip().split())
before = X

if abs(X)//D>=K:
  print(abs(X)-D*K)
else:
  for i in range(K):
    buf = X
    if X<0:
      X += D
    else:
      X -= D
    if X == before:
      if (K-i)%2 == 0:
        if X<0:
          X += D
        else:
          X -= D
      else:
        X = before
      break
    before=buf
  print(abs(X))
