a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
dx = abs(a - b)
ds = v - w
print("YES" if t * ds >= dx else "NO")

# よく見たら制約10の9乗だった
# i=0
# ans='NO'
# while i<t:
#     flg=a<b
#     if abs(a+v-b)<abs(a-v-b):
#         a+=v
#     else:
#         a-=v
#     if abs(b+w-a)<abs(b-w-a):
#         b-=w
#     else:
#         b+=w
#     if flg!=(a<b):
#         ans='YES'
#     i+=1
# print(ans)
