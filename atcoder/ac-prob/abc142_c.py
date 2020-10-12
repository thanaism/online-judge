n=int(input())
a=[*map(int,input().split())]
dic={i+1:v for i,v in enumerate(a)}
print(*[k for k,v in sorted(dic.items(),key=lambda x:x[1])])