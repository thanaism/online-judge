sx, sy, tx, ty = map(int, input().split())
dx = tx - sx
dy = ty - sy
ans = ''
ans += 'R' * dx
ans += 'U' * (dy + 1)
ans += 'L' * (dx + 1)
ans += 'D' * (dy + 1)
ans += 'R'
ans += 'D'
ans += 'R' * (dx + 1)
ans += 'U' * (dy + 1)
ans += 'L' * (dx + 1)
ans += 'D' * dy

print(ans)
