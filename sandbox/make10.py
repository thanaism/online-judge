"""
任意の4桁の数に対して、四則演算を組み合わせて10を生成可能なパターンを列挙する
ex) input : 9999 -> output : '(9*9+9)/9', '(9+9*9)/9'

Notes
-----
演算子の入る位置
  a|b|c|dの「|」位置に{+,-,*,/}が入るので4^3パターン
  数値の連結を許す場合は{+,-,*,/,␣}で空白を加える

2重カッコ
  数値の連結を許さなければ、必ず等値の数式があるので考慮不要?
  (A?B?(C?D)) -> 最外殻の()は無意味
  (A?(B?C))?D -> このパターンを考えればよい
  (A?(B?C)){+,-}D -> ()がなくてもよいので{*,/}に固定
  (A?(B{*,/}C)){*,/}D -> コレも無意味
  (A{*,/}(B{+,-}C))){*,/}D -> コレも無意味なのでやっぱり2重カッコは不要

以下の6パターンのみが有意?
  eq.      ->dig.   ->op.  ->pa.
  (a|b|c)|d->1,3,5,8->2,4,7->0,6
  a|(b|c|d)->0,3,5,7->1,4,6->2,8
  (a|b)|c|d->1,3,6,8->2,5,7->0,4
  a|(b|c)|d->0,3,5,8->1,4,7->2,6
  a|b|(c|d)->0,2,5,7->1,3,6->4,8
  (a|b|c|d)->1,3,5,7->2,4,6->0,8
"""



import re

def makeit(di,op,pa,s):
  ops=['+','-','/','*']
  ret=[]
  l=['']*9
  for i in ops:
    for j in ops:
      for k in ops:
        for ind,val in enumerate(di):
          l[val]=s[ind]
        for ind,val in enumerate(op):
          l[val]=(i,j,k)[ind]
        l[pa[0]],l[pa[1]]='(',')'
        e=''.join(l)
        # if any([
        #   re.search('\(\d+(\*|/)\d+(\*|/)\d+\)',e),
        #   re.search('(\+|-)\(\d(\+|-)\d(\+|-)\d\)',e),
        #   re.search('\(\d(\+|-)\d(\+|-)\d\)(\+|-)',e),
        #   # re.search('\(\d+(\+|-)\d+(\+|-)\d+\)',e),
        #   re.search('\(\d+(\*|/)\d+\)',e),
        #   re.search('(\+|-)\(.*\)$',e),
        #   re.search('^\(\d+(\+|-)\d+\)(\+|-)',e),
        #   re.search('\d+\(',e),
        #   re.search('\)\d+',e),
        #   re.search('\(\d+\)',e),
        #   re.search('(\+|-)\(.*\)(\+|-)',e),
        #   re.search('(\+|-|\*|/|\(|\)|^)0\d',e)
        #   ]):
        #   continue
        try:
          if eval(e)==10:
            ret+=remove_paren(e),
        except ZeroDivisionError:
            pass
  return ret

def remove_paren(e):
  """()を除去しても式の評価値が同じならその括弧は不要なので除去した結果を返す"""
  v=eval(e.translate(str.maketrans('','','()')))
  if v==eval(e):
    return v
  else:
    rerurn e

di_=[
  [1,3,5,8],
  [0,3,5,7],
  [1,3,6,8],
  [0,3,5,8],
  [0,2,5,7],
  [1,3,5,7]
]
op_=[
  [2,4,7],
  [1,4,6],
  [2,5,7],
  [1,4,7],
  [1,3,6],
  [2,4,6]
]
pa_=[
  [0,6],
  [2,8],
  [0,4],
  [2,6],
  [4,8],
  [0,8]
]

# すべての()の位置の組み合わせを列挙
def loop(s):
  s=str(s).zfill(4)
  res=[]
  for di,op,pa in zip(di_,op_,pa_):
    res+=makeit(di,op,pa,s),
  res=set(sum(res,[]))
  for m in res:
    print(m)


# 全パターン列挙
def show_all():
  for u in range(10000):
    s=str(u).zfill(4)
    loop(s)

# 単一インプットへの実行
def loop(s):
  s=str(s).zfill(4)
  res=[]
  for di,op,pa in zip(di_,op_,pa_):
    res+=makeit(di,op,pa,s),
  res=set(sum(res,[]))
  for m in res:
    print(m)
  if len(res)==0:
    print(None)

# 実行
# flg=input('single digits only? -> ')
loop(input('input? -> '),flg)