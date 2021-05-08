s=input()
f=int(s[:2])
b=int(s[2:])
if f>12 and b>12:
    print('NA')
elif (f==0 and b>12) or (b==0 and f>12):
    print('NA')
elif f==b==0:
    print('NA')
elif f==0:
    print('YYMM')
elif b==0:
    print('MMYY')
elif f>12:
    print('YYMM')
elif b>12:
    print('MMYY')
else:
    print('AMBIGUOUS')