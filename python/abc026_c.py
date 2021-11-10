n = int(input())
p = [[] for _ in range(n + 1)]
for i in range(n - 1):
    b = int(input())
    p[b].append(i + 2)


def dfs(i):
    if not p[i]:
        return 1
    salaries = []
    for j in p[i]:
        salaries.append(dfs(j))
    return max(salaries) + min(salaries) + 1


print(dfs(1))
