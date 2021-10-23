from collections import deque,defaultdict
import sys

def encode(i,j):
    if i<j: i,j=j,i
    return i*(i-1)//2 + j+1

def solve(n,a):
    endpoints = defaultdict(list)
    indegrees = defaultdict(int)
    for i in range(n):
        for j in range(1,n-1):
            s,t,u = i+1,a[i][j-1],a[i][j]
            x = encode(s,t)
            y = encode(s,u)
            endpoints[x].append(y)
            indegrees[y] += 1

    q = deque()
    decode = defaultdict(None)
    for i in range(n):
        for j in range(i+1,n):
            k = encode(i+1,j+1)
            decode[k] = (i+1,j+1)
            if indegrees[k]==0:
                q.append(k)
    s = set()
    cnt = 0
    ans = 1
    while q:
        i = q.popleft()
        x,y = decode[i]
        if x in s or y in s:
            s = set()
            ans += 1
        s.add(x); s.add(y)
        cnt += 1
        for j in endpoints[i]:
            indegrees[j] -= 1
            if indegrees[j]==0:
                q.append(j)
                
    if n*(n-1)//2>cnt: ans = -1
    print(ans)

def main():
    input = lambda: sys.stdin.readline().rstrip()
    n = int(input())
    a = [[*map(int,input().split())] for _ in range(n)]
    solve(n,a)

if __name__ == '__main__':
    main()