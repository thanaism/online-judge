n,k,*x=map(int,open(0).read().split())
print(sum((2*(k-i),2*i)[k-i>i] for i in x))