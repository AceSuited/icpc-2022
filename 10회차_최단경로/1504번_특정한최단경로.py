import heapq
import sys
input = lambda: sys.stdin.readline().strip()
inf = 10e6
n,e = map(int,input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    fro, to, cost = map(int,input().split())
    graph[fro].append((to,cost))
    graph[to].append((fro, cost))

v1, v2 = map(int,input().split())


def solve(start):
    heap = []
    visited = [False for _ in range(n + 1)]
    dist = [inf for _ in range(n+1)]
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:

        current_cost, current = heapq.heappop(heap)
        visited[current] = True
        for next, cost in graph[current]:
            if dist[next] > dist[current] + cost:
                dist[next] = dist[current] + cost
                heapq.heappush(heap, (dist[next], next))

    return dist


one_to_n = solve(1)
v1_to_n = solve(v1)
v2_to_n = solve(v2)


ans = min(one_to_n[v1] + v1_to_n[v2] + v2_to_n[n], one_to_n[v2] + v2_to_n[v1] + v1_to_n[n])

if ans >= 10e6:
    print(-1)
else:
    print(ans)