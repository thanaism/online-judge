n,m=map(int,input().split())
# グラフとコスト記録
g=[list() for _ in range(n)]
for _ in range(m):
    u,v,c=map(int,input().split())
    g[u-1].append((v-1,c))
    g[v-1].append((u-1,c))
# 全頂点ループ
from collections import deque
que=deque()
que.append(0)
digit=[0]*n
digit[0]=1
while que:
    i=que.popleft()
    p=digit[i]
    for v,c in g[i]:
        if digit[v]!=0:continue
        que.append(v)
        if c==p:
            digit[v]=(p+1 if p<n else p-1)
        else:
            digit[v]=c
# print(digit)
if digit.count(0):
    print('No')
    exit()
for i in digit:
    print(i)