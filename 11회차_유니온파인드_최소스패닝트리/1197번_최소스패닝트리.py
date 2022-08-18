import heapq
import sys
input = lambda:sys.stdin.readline().strip()

v, e = map(int,input().split())
roots = [i for i in range(v+ 1)]
edges = []
for _ in range(e):
    a,b,c =map(int,input().split())
    heapq.heappush(edges, (c,a,b))


def find(x):
    if x == roots[x]:
        return x
    else:
        roots[x] = find(roots[x])
        return roots[x]

def union(x,y):
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
total = 0
while cnt < v - 1:

    cost, fr, to = heapq.heappop(edges)
    if find(fr) != find(to):
        union(fr, to)
        total += cost
        cnt += 1

print(total)

