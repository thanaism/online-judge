from sys import stdin

N = int(stdin.readline().rstrip())
# print(N)
ary = []
for i in range(N):
    ary.append(int(stdin.readline().rstrip() * (10 ** 9)))
    # stdin.readline().rstrip().split()
    # print(ary[i])
cnt = 0

# def get_divisible_count(num,divider):
#   result = 0
#   while True:
#     if num%divider ==0:
#       result += 1
#       # num /= divider
#       num = int(num/divider)
#     else:
#       break
#   return result
def is_divisible(num, divider, times):
    result = 0
    while True:
        if result == times:
            return True
        elif num % divider == 0:
            result += 1
            # num /= divider
            num = int(num / divider)
        else:
            break
    return False


for i in range(N):
    for j in range(N - i - 1):
        num = ary[i] * ary[j + i + 1]
        if is_divisible(num, 2, 18):
            if is_divisible(num, 5, 18):
                cnt += 1
print(cnt)
