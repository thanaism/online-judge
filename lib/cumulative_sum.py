
# l[i]: 入力配列
# s[i]: [0,i)の半開区間の部分和

# itertoolsを使うのが一番速い
import itertools
l=[1]*1000
s=[*itertools.accumulate([0]+l)]
query=lambda i,j:s[j]-s[i]
print(query(20,200))

# 以下、速度検証
def time_test():
  import time

  def FOR(l):
    s=[0]
    for i in l:
      s.append(i+s[-1])
    # print(s[0],s[1],s[-2],s[-1])

  def LIS(l):
    s=[0]
    [i for i in range(len(l)) if s.append(s[i]+l[i])]
    # print(s[0],s[1],s[-2],s[-1])

  def NUM(l):
    import numpy
    s=[*numpy.cumsum([0]+l)]
    # print(s[0],s[1],s[-2],s[-1])

  def ITE(l):
    import itertools
    s=[*itertools.accumulate([0]+l)]
    # print(s[0],s[1],s[-2],s[-1])

  l=[1]*50000

  def TIM(f):
    st=time.time()
    for i in range(100):
      f()
    print(time.time()-st)

  TIM(lambda:FOR(l))
  TIM(lambda:LIS(l))
  TIM(lambda:NUM(l))
  TIM(lambda:ITE(l))
  # 0.7299740314483643
  # 0.8644957542419434
  # 1.0461170673370361
  # 0.26815319061279297