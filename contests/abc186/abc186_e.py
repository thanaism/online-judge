t=int(input())
def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)
for _ in range(t):
    n,s,k=map(int,input().split())
    r=k%n
    m=n-s
    if r==0:
        print(-1)
    elif m%r!=0 and n%r==0:
        print(-1)
    # elif m%r==0:
        # print(m//r)
    else:
        print(lcm(m,r)//m)
        