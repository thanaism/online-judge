from itertools import combinations
a,b,c,d=map(int,input().split())
s=sum([a,b,c,d])
flg=False
for i in range(1,4):
 for cmb in combinations([a,b,c,d],i):
  if sum(cmb)==s-sum(cmb):
   flg=True
print(['No','Yes'][flg])

"""
選ぶのは2つと限らず1つ以上の記述を見逃した
setで管理して同じ値があることを考慮していなかった
[e for e in l if e not in cmb]に変えたけど同じミス
結果、めっちゃペナルティ
"""