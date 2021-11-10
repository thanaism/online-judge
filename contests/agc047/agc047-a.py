# from sys import stdin
# N = int(stdin.readline().rstrip())
# # print(N)
# ary=[]
# for i in range(N):
#   ary.append(float(stdin.readline().rstrip()))
#   # stdin.readline().rstrip().split()
#   # print(ary[i])
# cnt = 0
def get_divisible_count(num, divider):
    result = 0
    while True:
        if num % divider == 0:
            result += 1
            # num /= divider
            num = int(num / divider)
        else:
            break
    return result


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


print(get_divisible_count(27, 3))
print(is_divisible(27, 3, 4))

# for i in range(N):

#   for j in range(N-i-1):
#     # print(i,j+i+1)
#     # print(ary[i],ary[i+j+1],(((ary[i]%1)*(ary[j+i+1])%1)))
#     if ((ary[i]%1)*(ary[j+i+1]%1))%1 == 0:
#       cnt += 1
# print(cnt)
