# 漸化式がすぐに求まる
# a[n+1] = 10*a[n]+7, a[1] = 7

# 漸化式で表すことができるので剰余に循環性がある
# Kでの剰余の種類は0からK-1までの範囲となる
# mod Kを順に求めていき0のときのインデックスを出力
# 時間が厳しければ重複が生じた時点でループを抜ける処理を追加

from sys import stdin
K = int(stdin.readline().rstrip())
def main(K):
  a=0
  for i in range(K):
    a = ((10%K) * a + 7)%K
    if a == 0:
      return i + 1
  return -1
print(main(K))



