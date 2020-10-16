# l[i]: 入力配列

l=[*range(3)]
import itertools as I
for i in I.permutations(l):
  print(i)

# 自力で実装してみる
# def permutations(l,n=None):
#   r=len(l)
#   n=r if n is None else n
#   if n>r:return
#   idx=[*range(r)]
#   pos=idx[r+1:r-n:-1]
#   yield tuple(l[i] for i in idx[:n])
#   while r:
#     for i in reversed(range(n)):
#       pos[i]-=1
#       if pos[i]==0:
#         idx[i:]=idx[i+1:]+idx[i:i+1]
#         pos[i]=r-i
#       else:
#         j=pos[i]
#         idx[i],idx[-j]=idx[-j],idx[i]
#         yield tuple(l[i] for i in idx[:n])
#         break
#     else:return

def next_permutation(l):
  n=len(l)
  i=n-1
  while l[i-1]>l[i]:
    i-=1
    if i==0:break
  if i==0:return False
  j=i
  while j+1<n and l[i-1]<l[j+1]:
    j+=1
  l[i-1],l[j]=l[j],l[i-1]
  p,q=i,n-1
  while q-p>0:
    l[p],l[q]=l[q],l[p]
    p+=1
    q-=1
  return True

f=['a','b','c','d']
f=[1,2,3,4,5]

print(f)
while next_permutation(f):
  print(f)


# m=permutations(l)
# print(next(m))
# print(next(m))

# print(next(permutations(l)))
# print(next(permutations(l)))
# print(next(permutations(l)))
# print(next(permutations(l)))
# print(next(permutations(l)))



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