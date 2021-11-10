a, b, c = map(int, input().split())
if a == b:
    if c == 0:
        print("Aoki")
    else:
        print("Takahashi")
else:
    if a == max(a, b):
        print("Takahashi")
    elif b == max(a, b):
        print("Aoki")
