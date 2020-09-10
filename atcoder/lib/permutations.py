# l[i]: 入力配列

l=[*range(3)]
import itertools as I
for i in I.permutations(l):
  print(i)


# 以下、動作確認時のコメントアウト保存用
 
# for i in (i for i in I.permutations(l)):
#   print(i)

# p=[*I.permutations(l)]
# print(p)

# [_ for _ in range(3) if print(next(I.permutations(l)))]

# s=[]
# s.append(next(I.permutations(l)))
# s.append(next(I.permutations(l)))
# s.append(next(I.permutations(l)))
# print(s)

# print(type(I.permutations(l)))

# gen = (i for i in I.permutations(l))
# print(next(gen))

# for i in gen:
#   print(i)

# while i:=next(gen):
#   print(i)

# print(gen.send([1,2]))