# n=int(input())
# s=input()
# ans=0
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             f1=f2=f3=False
#             for l in s:
#                 if f1==False and l==str(i):
#                     f1=True
#                     continue
#                 if f2==False and f1 and l==str(j):
#                     f2=True
#                     continue
#                 if f3==False and f1 and f2 and l==str(k):
#                     f3=True
#                     continue
#             if f1 and f2 and f3:ans+=1
# print(ans)

# n=int(input())
# s=input()
# a=set()
# for i in range(1<<n):
#   t=bin(i)[2::]
#   t='0'*(n-len(t))+t
#   if t.count('1')!=n-3:continue
#   u=''
#   for j in range(n):
#     if t[j]=='0':
#       u+=s[j]
#   a|={u}
# print(len(a))

# def main():
#     n=int(input())
#     s=input()
#     ans=0
#     for i in range(1000):
#         t=f'{i:03d}'
#         k=0
#         for j in range(n):
#             if s[j]==t[k]:k+=1
#             if k==3:break
#         if k==3:ans+=1
#     print(ans)
# main()

n = int(input())
s = input()
ans = 0
for i in range(1000):
    # t=f'{i:03d}'
    t = str(i).zfill(3)
    k = 0
    for j in range(n):
        if s[j] == t[k]:
            k += 1
        if k == 3:
            break
    if k == 3:
        ans += 1
print(ans)
