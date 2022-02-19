import sys
input = lambda:sys.stdin.readline().strip()

n,m = map(int,input().split())
inf = -10e6
graph = [[] for _ in range(n+1)]
distance = [inf for _ in range(n+1)]
router = [-1 for _ in range(n+1)]
negative_cycle = [-1 for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

distance[1] = 0
isNegative = False
for iter in range(n):
    for current in range(1,n+1):
        for next, cost in graph[current]:
            if distance[current] != inf and distance[current] + cost > distance[next]:
                if iter == n - 1:
                    isNegative = True
                    distance[next] = distance[current] + cost

                else:
                    distance[next] = distance[current] + cost
                    router[next] = current

if isNegative:
    temp = []

    for i in range(1, n):
        cnt = 0
        idx = i
        while cnt <= n:
            temp.append(router[idx])
            idx = router[idx]
            cnt += 1
    temp = set(temp)
    if router[n] in temp:
        print(-1)
else:
    if router[n] == -1:
        print(-1)
        sys.exit()
    res = []
    res.append(n)
    idx = n
    while True:
        if idx == 1:
            break
        res.append(router[idx])
        idx= router[idx]

    res.reverse()
    print(*res)


