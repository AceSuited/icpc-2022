import sys
import math
input = lambda:sys.stdin.readline().strip()

n,m = map(int,input().split())
inf = math.inf
graph = [[] for _ in range(n+1)]
distance = [-inf for _ in range(n+1)]
router = [-1 for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

distance[1] = 0
for iter in range(n):
    for current in range(1,n+1):
        for next, cost in graph[current]:
            if distance[current] != -inf and distance[current] + cost > distance[next]:

                distance[next] = distance[current] + cost
                router[next] = current
                if iter == n- 1:
                    distance[next] = inf

res = [n]

if distance[n] != inf:
    current = n
    while current != 1:
        current = router[current]
        res.append(current)

    res.reverse()
    print(*res)
else:
    print(-1)