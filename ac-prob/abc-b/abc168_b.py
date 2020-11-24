k=int(input())
s=input()
print(f'{s[:k]}...' if len(s)>k else s)