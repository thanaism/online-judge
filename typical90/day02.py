n=int(input())
for i in range(1<<n):
    s=bin(i)[2:].zfill(n)
    if s.count('0')==s.count('1'):
        r=l=0
        ok=True
        for j in range(n):
            if (i>>j)&1:
                r+=1
            else:
                l+=1
            if r>l:ok=False
        if ok:
            print(s.replace('0', ')').replace('1', '('))