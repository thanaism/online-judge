n,m=map(int,input().split())
v=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    v[a-1].append(b-1)
    v[b-1].append(a-1)
ans=0
# for i in range(3**n):
#     s=''
#     for j in range(n):
#         state=(i//(3**j))%3
#         s+=str(state)
#     f=True
#     for j in range(n):
#         for k in v[j]:
#             if s[k]==s[j]:
#                 f=False
#                 break
#             if not f:break
#     if f:ans+=1
s=[]
def dfs(x,l):
    l.append(x)
    f=True
    for i in v[x]:
        if i not in l:
            f=False
            dfs(i)
    if f:s.append(l)

for i in range(n):
    dfs(i)

def paint(x,color,ls):
    if x==len(ls)-1:
        return None
    for i in v[x]:
        if  
for i in s:
    




print(ans)