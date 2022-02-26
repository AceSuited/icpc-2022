import heapq
import sys, math
inf = math.inf
input = lambda:sys.stdin.readline().strip()

n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append([e, c])
    graph[e].append([s, c])

def trav(start, blocked_edge):
    queue = []
    visited = [False for _ in range(n+1)]
    distance = [inf for _ in range(n+1)]

    s, e = blocked_edge
    router = []

    heapq.heappush(queue,(0,start, [start]))
    distance[start] = 0
    while queue:
        current_cost, current, path = heapq.heappop(queue)

        if visited[current]:
            continue
        if current == n:
            router = path
        visited[current] = True
        for next, next_cost in graph[current]:
            if not visited[next] and distance[next] > distance[current] + next_cost:
                if (current == s and next == e) or (current == e and next == s):
                    continue
                distance[next] = distance[current] + next_cost
                heapq.heappush(queue, (distance[next], next, path + [next]))


    return distance, router

origin_time,router = trav(1, (0,0))

res = []
toBlock = []
if origin_time[n] == inf:
    print(-1)
    sys.exit()
for i in range(len(router) - 1):
    toBlock.append((router[i], router[i + 1]))

for edge in toBlock:
    temp = trav(1, edge)[0][n]
    res.append(temp)

res = max(res) - origin_time[n]


if res == inf:
    print(-1)
else:
    print(res)