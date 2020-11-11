_=input();l=sorted([*map(int,input().split())])
print('YNeos'[l[-1]>=sum(l[:-1])::2])