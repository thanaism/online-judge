import timeit

# def basic_eratosthenes(n):
  # """エラトステネスの篩：2からnまでの順列から素数の倍数をふるい落とす"""
  # # 2からnまでの順列を用意する
  # # n=int(input())
  # l = range(2,n+1)
  # # 最大値の平方根より大きくなることはない
  # # 大量の平方根を計算する場合は速度面でmath.sqrt()も検証すること
  # # r = n**0.5
  # # 1 + 切り捨て処理(math.floorと値は同じになるが型はfloat)
  # # r = 1 + r//1
  # # 参考：切り上げ処理(math.ceilと値は同じになるが型はfloat)
  # # r = -(-r//1)
  # k=0
  # while l[k]**2<=n:
  #   # print((l:=sorted(list(set(l)-{i for i in l if not i%l[k] and i!=l[k]}))))
  #   # l=sorted(list(set(l)-{i for i in l if not i%l[k] and i!=l[k]}))
  #   l=list(set(l)-{i for i in l if not i%l[k] and i!=l[k]})
  #   # l=[*(set(l)-{i for i in l if not i%l[k] and i!=l[k]})]
  #   l.sort()
  #   k+=1
  # print(len(l))

  # n=int(input())
  # if n<2:
  #   print(0)
  # else:
  #   l = range(2,n+1)
  #   k=0
  #   while l[k]**2<=n:
  #     l=list(set(l)-{i for i in l if not i%l[k] and i!=l[k]})
  #     l.sort()
  #     k+=1
  #   print(len(l))
  # n=int(input())

  # if n<2:
  #   print(0)
  # else:
  #   p=[2]
  #   if n==2:
  #     l=[]
  #   else:
  #     l = range(3,n+1,2)
  #     while l[0]**2<=n:
  #       p.append(k:=l[0])
  #       l=list(set(l)-{i for i in l if not i%k})
  #       # l.sort()
  #   print(len(p+l))
  #   # print(p+l)

# n=int(input())
# n=str(n)


def base_1(n):
  """
  エラトステネスの篩（N**未満**の素数の個数を数える）
  10^7=1752ms,10^8=19575ms
  """
  b=[1]*n
  b[0]=b[1]=0
  m=int(-(-(n**0.5)//1))
  for i in range(2,m):
    if b[i]:
      for j in range(i*i,n,i):
        b[j]=0
  print(sum(b))
  # print([i for i,j in enumerate(''.join(map(str,b))) if j=='1'])

def base_2(n):
  """リスト内包表記化：10^7=10267ms"""
  # 5倍以上もとより遅いのでロジック見直しが必要
  b=[1]*n
  b[0]=b[1]=0
  m=int(-(-(n**0.5)//1))
  for k in [j for i in range(2,m) if b[i] for j in range(i*i,n,i)]:
    b[k]=0
  print(sum(b))

def base_3(n):
  """偶数の省力化：10^7=771ms,10^8=8705ms"""
  b=[1]*(n//2)
  b[0]=0
  m=int(-(-(n**0.5)//1)//2)
  for i in range(1,m):
    if b[i]:
      t=2*i+1  #フラグを奇数2k+1に対応させる
      for j in range(2*i*(i+1),int(n//2),t):
        b[j]=0
  print(sum(b)+1)  #2自身はフラグに含まれないので数に足す

def base_4(n):
  """
  2,3,5の省力化：

  摘要
  −−−−
  2を除いて残る候補->2k+1
  3を除いて残る候補->3k+{1,2}
  5を除いて残る候補->5k+{1,2,3,4}
  
  2,3を除いて残る候補->6k+{1,5}
  2,3,5を除いて残る候補->30k+{1,7,11,13,17,19,23,29}
  {}の中がちょうど8パターンになる->1バイトで表現できる

  (30k+m)^2 = (30k)^2 + 2*30km +m^2
  これを各項30で割ってバイト単位に振り直すと、
  30 * {k(30k+2m)+(m^2)//30} + (m^2 mod 30)

  """
  pass

f=lambda: base_1(10**7)
LOOPS=1
print(f"{int(timeit.timeit(f,globals=globals(),number=LOOPS)/LOOPS*1000)} ms")
