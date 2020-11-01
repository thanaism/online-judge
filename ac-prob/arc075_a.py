n=int(input())
s=[int(input()) for _ in range(n)]
def main():
  if sum(s)%10!=0:
    return sum(s)
  else:
    for i in sorted(s):
      if i%10!=0:
        return sum(s)-i
    return 0
print(main())
