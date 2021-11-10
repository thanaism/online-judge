# def prime_factorize(n):
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1:
#         a.append(n)
#     return a
# n=int(input())
# l=prime_factorize(n)
# if len(l)==0:
#     l=[1]
# # print(l)
# ll=len(l)
# ans=set()
# for i in range(1<<ll):
#     s=bin(i)[2:].zfill(ll)
#     # print(s)
#     x=1
#     y=1
#     for j in range(ll):
#         if s[j]=='1':
#             x*=l[j]
#         else:
#             y*=l[j]
#     if x>y:x,y=y,x
#     print(x*y)
#     ans|={(x,y)}
# # print(ans)
# print(len(ans))
n = int(input()) * 2
ans = 0
for i in range(1, n + 1):
    if i * i > n:
        break
    if n % i == 0:
        a, b = i & 1, (n // i) & 1
        if a ^ b:
            ans += 1
print(ans * 2)
