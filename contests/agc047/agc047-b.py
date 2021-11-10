from sys import stdin

N = int(stdin.readline().rstrip())

ary = []
for i in range(N):
    ary.append(str(stdin.readline().rstrip()))

cnt = 0


def compareStr(str1, str2):
    # print(str1,str2)
    if str1 == str2:
        return True
    elif len(str1) > 1:
        if compareStr(str1[0] + str1[2:], str2):
            # print(str1[0]+str1[2:],str2)
            return True
        elif compareStr(str1[1] + str1[2:], str2):
            # print(str1[1]+str1[2:],str2)
            return True
        else:
            return False
    else:
        return False


for i in range(N):
    for j in range(N - i - 1):
        # print(i,j+i+1)
        # print(ary[i],ary[i+j+1])
        if compareStr(ary[i], ary[i + j + 1]):
            cnt += 1
        elif compareStr(ary[i + j + 1], ary[i]):
            cnt += 1

print(cnt)
