x,k,d = [abs(int(i)) for i in input().rstrip().split()]
print (max(x-k*d,(x%d,d-x%d)[k-x//d&1]))