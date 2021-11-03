r, c, k = map(int, input().split())
n = int(input())
rc = [[*map(lambda i: int(i) - 1, input().split())] for _ in range(n)]

candies_in_row = [0] * r
candies_in_col = [0] * c
for row, col in rc:
    candies_in_row[row] += 1
    candies_in_col[col] += 1

row_count = [0] * (n + 1)
col_count = [0] * (n + 1)
for i in candies_in_row:
    row_count[i] += 1
for i in candies_in_col:
    col_count[i] += 1

ans = 0
for i in range(k + 1):
    ans += row_count[i] * col_count[k - i]

for row, col in rc:
    if candies_in_row[row] + candies_in_col[col] == k:
        ans -= 1
    if candies_in_row[row] + candies_in_col[col] == k + 1:
        ans += 1

print(ans)
