import heapq
import sys
input = lambda: sys.stdin.readline().strip()
t = int(input())
inf = 10e9

for case in range(t):
    n, m = map(int, input().split())
    relations = [[] for _ in range(m)]
    visited = [False for _ in range(m)]
    distance = [inf for _ in range(m)]
    heap = []
    for _ in range(n):
        fro, to, cost = map(int,input().split())
        relations[fro].append((to,cost))
        relations[to].append((fro,cost))

    start, end = 0, m-1
    distance[start] = 0
    heapq.heappush(heap, (0, start, [start]))

    found = False
    while heap:
        cost_current, current, path = heapq.heappop(heap)

        if current == end:
            print("Case #%d:" % (case + 1), end=" ")
            print(*path)
            found = True
            break

        if visited[current]:
            continue
        visited[current] = True
        for next, cost in relations[current]:
            dist = cost + distance[current]
            if dist < distance[next]:
                distance[next] = dist
                heapq.heappush(heap, (distance[next], next, path + [next]))

    if not found:
        print("Case #%d:" % (case + 1), end=" ")
        print(-1)