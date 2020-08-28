n=input()
a=sorted(map(int,input().split()))
print(sum(a[::-2])-sum(a[-2::-2]))