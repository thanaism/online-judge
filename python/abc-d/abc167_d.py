n, k = map(int, input().split())
a = [*map(int, input().split())]

cnt = 0
now = 0
seen = set()
seen.add(0)
while True:
    last_town = now + 1
    if cnt < k:
        cnt += 1
    else:
        break
    now = a[now] - 1
    if now in seen:
        if cnt == k:
            print(now + 1)
            exit()
        break
    else:
        seen.add(now)

if cnt == k:
    print(last_town)
    exit()

loop_cnt = 0
start = now
while True:
    loop_cnt += 1
    start = a[start] - 1
    if start == now:
        break

remain = (k - cnt) % loop_cnt
cnt = 0
while True:
    last_town = now + 1
    if cnt < remain:
        cnt += 1
    else:
        break
    now = a[now] - 1

print(last_town)
