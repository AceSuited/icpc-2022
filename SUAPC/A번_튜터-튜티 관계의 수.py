import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
roots = [i for i in range(n + 1)]

def find(x):
    if roots[x] == x:
        return x
    else:
        roots[x] = find(roots[x])
        return roots[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if y == x:
        return
    else:
        if y < x:
            roots[x] = y
        else:
            roots[y] = x



for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    union(u, v)
    union(v, u)


dic = dict()
for i in range(1, n + 1):
    if roots[i] not in dic:
        dic[roots[i]] = [i]
    else:
        dic[roots[i]].append(i)

ans = 1
for key in dic.keys():
    if len(dic[key]) != 0:
        ans = ans * len(dic[key])
        ans = ans % 1000000007

print(ans % 1000000007)
