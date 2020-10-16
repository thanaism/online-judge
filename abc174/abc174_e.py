from sys import stdin

N, K = map(int, input().rstrip().split())
A = [int(x) for x in stdin.readline().rstrip().split()]

def is_ok(x):
  count = 0
  for ln in A:
    count += ln//x
    if count > K:
      return False
  return True

def binary_search(ng,ok):
  while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
  return ok

print(binary_search(0,max(A)))