n=int(input())
from collections import defaultdict
v=defaultdict(list)
vs=[]
for _ in range(n-1):
    a,b=map(int,input().split())
    vs.append((a,b))
    v[a].append(b)
    v[b].append(a)
c=defaultdict(int)
q=int(input())
from collections import deque
for _ in range(q):
    t,e,x=map(int,input().split())
    a,b=vs[e]
    if t!=1:a,b=b,a
    que=deque()
    que.append(a)
    while que:
        i=que.popleft()
        c[i]+=x
        for j in v[i]:
            if j!=b and j!=i:
                que.append(j)
                c[j]+=x
for i in c:
    print(i)