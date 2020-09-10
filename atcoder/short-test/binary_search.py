def is_ok(x):
  # ここに判定を書く
  if ng:
      return False
  return True

def binary_search(ng,ok):
  # 範囲は[ok,ng)または(ng,ok]の半開区間
  while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
  return ok