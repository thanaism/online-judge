n = int(input())

x = 2
d = 0
while x < n:
    x <<= 1
    d += 1
x = 1

if d==0 or d & 1:
    while x <= n:
        x *= 2
        if x > n:
            print('Aoki')
            break
        x *= 2
        x += 1
        if x > n:
            print('Takahashi')
else:
    while x <= n:
        x *= 2
        x += 1
        if x > n:
            print('Aoki')
            break
        x *= 2
        if x > n:
            print('Takahashi')
