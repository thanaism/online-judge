# def main():
#     n=int(input())
#     l=set()
#     for _ in range(n):
#         l|={tuple(map(int,input().split()))}
#     ans=0
#     for i in l:
#         for j in l:
#             a,b=i
#             c,d=j
#             dx,dy=c-a,b-d
#             e,f=c-dy,d-dx
#             g,h=a-dy,b-dx
#             if not (e,f) in l:continue
#             if not (g,h) in l:continue
#             ans=max(ans,dx*dx+dy*dy)
#     return ans
# print(main())


def main():
    n = int(input())
    p = set()
    q = []
    for _ in range(n):
        x, y = map(int, input().split())
        p |= {(x, y)}
        q.append([x, y])
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = q[i]
            x2, y2 = q[j]
            dx = x2 - x1
            dy = y1 - y2
            x3, y3 = x2 - dy, y2 - dx
            x4, y4 = x1 - dy, y1 - dx
            if (x3, y3) not in p:
                continue
            if (x4, y4) not in p:
                continue
            ans = max(ans, dx * dx + dy * dy)
    return ans


print(main())
