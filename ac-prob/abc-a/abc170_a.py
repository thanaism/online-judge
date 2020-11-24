x=[*map(int,input().split())]
print(sum([i+1 for i in range(5) if x[i]==0]))