import heapq
import sys

input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())

generator = list(map(int, input().split()))
edges = []
roots = [i for i in range(n + 1)]
for gen in generator:
    roots[gen] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    heapq.heappush(edges, (w, u, v))


def find(x):
    if roots[x] == x:
        return x
    else:
        roots[x] = find(roots[x])
        return roots[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    else:
        if x < y:
            roots[y] = x
        else:
            roots[x] = y


cnt = 0
ans = 0

while cnt < n - len(generator):
    cost, a, b, = heapq.heappop(edges)
    if find(a) != find(b):
        union(a,b)
        cnt += 1
        ans += cost


print(ans)
