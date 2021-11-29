n = int(input())
raining = [0] * (60 * 30)
for _ in range(n):
    (sh, sm), (eh, em) = map(lambda x: (int(x[:2]), int(x[2:])), input().split("-"))
    sm = sm // 5 * 5
    em = -(-em // 5) * 5
    eh += em // 60
    em %= 60
    raining[sh * 60 + sm] += 1
    raining[eh * 60 + em] -= 1

for i in range(1, 60 * 30):
    raining[i] += raining[i - 1]

started = False
for i in range(60 * 30):
    h = i // 60
    m = i % 60
    if raining[i] == 0:
        if started:
            print(f"{h:02d}{m:02d}")
            started = False
            continue
        else:
            continue
    if not started:
        started = True
        print(f"{h:02d}{m:02d}-", end="")
