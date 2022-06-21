n = int(input())
s = [input() for _ in range(n)]


def search(x, y):
    result = True
    for i in range(x, x + 6):
        cnt = 0
        for j in range(y, y + 6):
            if s[i][j] == ".":
                cnt += 1
        if cnt <= 2:
            result = False
            break
    for j in range(y, y + 6):
        cnt = 0
        for i in range(x, x + 6):
            if s[i][j] == ".":
                cnt += 1
        if cnt <= 2:
            result = False
            break
        cnt1 = cnt2 = 0
        for i in range(6):
            if s[x + i][y + i] == ".":
                cnt1 += 1
            if s[x + i][y + 5 - i] == ".":
                cnt2 += 1
        if cnt1 <= 2 or cnt2 <= 2:
            result = False
    return result


ans = "No"
for i in range(n - 5):
    for j in range(n - 5):
        if not search(i, j):
            ans = "Yes"
            break

print(ans)
