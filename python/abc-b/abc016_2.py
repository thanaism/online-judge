a, b, c = map(int, input().split())
if a + b == a - b == c:
    print("?")
elif a + b == c:
    print("+")
elif a - b == c:
    print("-")
else:
    print("!")
