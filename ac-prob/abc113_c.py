n,m=map(int,input().split())
p=[[*map(int,input().split()),i] for i in range(m)]
q=sorted(p,key=lambda x:x[1])
ans=['']*100001
cnt=[0]*100001
for i in q:
  cnt[i[0]]+=1
  ans[i[2]]=f'{i[0]:06d}{cnt[i[0]]:06d}'
for i in p:
  print(ans[i[2]])