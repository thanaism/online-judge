from sys import stdin

N = int(stdin.readline().rstrip())
# print(N)
L = [int(x) for x in stdin.readline().rstrip().split()]
# print(L)
count = 0
for i in range(N):
    for j in range(i, N):
        if L[j] != L[i]:
            for k in range(j, N):
                if L[k] != L[i] and L[k] != L[j]:
                    if L[i] == max(L[i], L[j], L[k]):
                        # print('i')
                        if L[i] < L[j] + L[k]:
                            # print(i+1,j+1,k+1)
                            count += 1
                    elif L[j] == max(L[i], L[j], L[k]):
                        # print('j')
                        if L[j] < L[i] + L[k]:
                            # print(i+1,j+1,k+1)
                            count += 1
                    elif L[k] == max(L[i], L[j], L[k]):
                        # print('k')
                        if L[k] < L[j] + L[i]:
                            # print(i+1,j+1,k+1)
                            count += 1
print(count)
