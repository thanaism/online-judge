n=int(input())
s=[]
for _ in range(n):
  s.append(input())
memo=[]

def remove(d,i):
  for j,v in enumerate(s[i]):
    if (j not in d) and v=='1':
      d|={j}
      remove(d,j)

def dfs(deleted,cnt):
  if len(deleted)==n:
    memo.append(cnt)
    return
  for i,v in enumerate(s):
    if i not in deleted:
      d=deleted.copy()
      d|={i}
      remove(d,i)
      dfs(d,cnt+1)
dfs(set(),0)
print(sum(memo)/len(memo))