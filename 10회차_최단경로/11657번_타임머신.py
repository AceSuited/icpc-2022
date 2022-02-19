import sys
input = lambda:sys.stdin.readline().strip()

n,m = map(int,input().split())

inf = 10e9

distance =[inf for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    fro, to, cost = map(int,input().split())
    graph[fro].append((to,cost))

distance[1] = 0
isThereNegative = False
for _ in range(n):
    for current in range(1, n + 1):
        for next, cost in graph[current]:
            if distance[current] + cost < distance[next]:
                distance[next] = distance[current] + cost
                if _ == n - 1:
                    isThereNegative = True

if isThereNegative:
    print(-1)
else:
    for i in range(2,n + 1):
        if distance[i] == inf:
            print(-1)
        else:
            print(distance[i])


