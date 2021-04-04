n=int(input())
for i in range(1<<n):
    if bin(i).count('0')==bin(i).count('1')+1:
        p=0
        f=True
        for j in range(n):
            if (i>>j)&1:
                p+=1
            else:
                p-=1
                if p<0:f=False
        if f:
            print(bin(i))