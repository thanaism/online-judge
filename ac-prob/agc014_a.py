# 163Byte
# a,b,c=map(int,input().split())
# if a==b==c and a%2==0:
#   print(-1)
# else:
#   res=0
#   while a%2==b%2==c%2==0:
#     a,b,c=(b+c)/2,(c+a)/2,(a+b)/2
#     res+=1
#   print(res)

# 83Byte
# a,b,c=map(int,input().split())
# f=lambda x:len(bin(x&-x))-3
# print(f(a-b|b-c)or~c%-2)

# Attempts to shorten lambda functions
# f=lambda x:len(f'{x&-x:b}')-1
# f=lambda x:len(bin(x&-x))-3
# f=lambda x:(x&-x).bit_length()-1
# f=lambda x:bin(x&-x)[::-1].find('1')

# 76Byte
# a,b,c=map(int,input().split());print(((e:=a-b|b-c)!=b&1)*len(f'{e&-e:b}')-1)

# 72Byte
a,b,c=map(int,input().split());print(len(bin((e:=a-b|b-c)&-e))-3or~c%-2)