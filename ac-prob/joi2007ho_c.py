def main():
    n=int(input())
    l=set()
    for _ in range(n):
        l|={tuple(map(int,input().split()))}
    ans=0
    for i in l:
        for j in l:
            a,b=i
            c,d=j
            dx,dy=c-a,b-d
            e,f=c-dy,d-dx
            g,h=a-dy,b-dx
            if not (e,f) in l:continue
            if not (g,h) in l:continue
            ans=max(ans,dx*dx+dy*dy)
    return ans
print(main())