# a,b,c=map(int,input().split())
# # # a=[*map(int,input(),split())]
# # # *a,map(int,input(),split())
# # # f=lambda x:len(f'{x&-x:b}')-1
# # # f=lambda x:len(bin(x&-x))-3
# f=lambda x:(x&-x).bit_length()-1
# # # f=lambda x:bin(x&-x)[::-1].find('1')
# # # e=a-b|b-c
# print(f(a-b|b-c)or~c%-2)

# print(len(bin((e:=a-b|b-c)&-e))-3or~a%-2)
# # if a==b==c and a%2==0:
# #   print(-1)
# # else:
# #   res=0
# #   while a%2==b%2==c%2==0:
# #     a,b,c=(b+c)/2,(c+a)/2,(a+b)/2
# #     res+=1
# #   print(res)

# a,b,c=map(int,input().split());print(len(bin((e:=a-b|b-c)&-e))-3or~c%-2)

a,b,c=map(int,input().split());print(((e:=a-b|b-c)!=b&1)*len(f'{e&-e:b}')-1)