# a=sorted(map(int,[*open(0)][1].split()));print(sum(a[::-2])-sum(a[-2::-2]))
# _,a=open(0);a=sorted(map(int,a.split()));print(sum(a[::-2])-sum(a[-2::-2]))

# _,a=open(s:=0);[(s:=i-s)for i in sorted(map(int,a.split()))];print(s)

_,a=open(s:=0)
for i in sorted(map(int,a.split())):s=i-s
print(s)