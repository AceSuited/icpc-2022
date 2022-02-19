import heapq
import sys
input = lambda:sys.stdin.readline().strip()
inf = 10e9

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    fro, to, cost = map(int,input().split())
    graph[fro].append((to,cost))

start,end = map(int,input().split())




distance = [inf for _ in range(n+1)]
visited = [False for _ in range(n+1)]
prev = [ -1 for _ in range(n+1)]
heap = []
distance[start] = 0
heapq.heappush(heap, (0,start,[start]))

while heap:
    cost_current, current,path = heapq.heappop(heap)
    if visited[current]:
        continue

    if current == end:
        print(cost_current)
        print(len(path))
        print(*path)
        break
    visited[current] = True
    for next, cost in graph[current]:
        if not visited[next] and distance[next] > cost_current + cost:
            distance[next] = cost_current + cost
            prev[next] = current
            heapq.heappush(heap, (distance[next], next,path+[next]))



