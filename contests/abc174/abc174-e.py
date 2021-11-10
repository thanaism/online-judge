from sys import stdin
from math import floor, ceil

N, K = map(int, input().rstrip().split())
A = [int(x) for x in stdin.readline().rstrip().split()]


def is_max_len_less_than_input(x, K, A):
    count = 0
    # if x==0:
    #   return False
    # 区間は(ng, OK]の半開区間のため、0除算の回避は不要
    for ln in A:
        count += ceil(ln / x) - 1
    if count > K:
        return False
    return True


def binary_search(begin, end, K, A):
    while abs(end - begin) > 1:
        mid = (begin + end) // 2
        if is_max_len_less_than_input(mid, K, A):
            end = mid
        else:
            begin = mid
    return end


print(binary_search(0, max(A), K, A))
# 最小値は0：(ng, OK]の半開区間のため、0除算の回避は不要
