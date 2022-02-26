import heapq
import sys
input = lambda:sys.stdin.readline().strip()
n,m,x = map(int,input().split())
inf = 10**7
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append((e,c))



def trav(start, end):
    visited= [False for _ in range(n+1)]
    dist = [inf for _ in range(n+1)]
    dist[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))
    while queue:
        current_cost, current= heapq.heappop(queue)
        if current == end:
            return current_cost

        visited[current] = True

        for next, next_cost in graph[current]:

            if not visited[next] and dist[next] > current_cost + next_cost:
                dist[next] = current_cost + next_cost
                heapq.heappush(queue, (dist[next], next))
    return dist[end]
res = []
for i in range(1, n+ 1):
    res.append(trav(i, x) + trav(x, i))
print(max(res))