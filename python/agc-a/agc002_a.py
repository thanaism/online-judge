a, b = map(int, input().split())
if a <= 0 <= b:
    print("Zero")
elif 0 < a <= b:
    print("Positive")
elif a <= b < 0:
    if (b - a) % 2 == 0:
        print("Negative")
    else:
        print("Positive")
