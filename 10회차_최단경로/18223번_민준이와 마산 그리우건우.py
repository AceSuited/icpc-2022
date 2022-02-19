import heapq

v,e,p = map(int,input().split())
inf = 10e6

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    fro, to, cost = map(int,input().split())
    graph[fro].append((to,cost))
    graph[to].append((fro,cost))


def trav(start, end):
    heap = []
    visited = [False for _ in range(v + 1)]
    distance = [inf for _ in range(v + 1)]
    heapq.heappush(heap, (0, start, [start]))
    distance[start] = 0

    while heap:
        cost_current, current, path = heapq.heappop(heap)
        if visited[current]:
            continue
        if current == end:
            return path, cost_current
        visited[current] = True
        for next, cost_next in graph[current]:
            dist = distance[current] + cost_next
            if dist < distance[next]:
                distance[next] = dist
                heapq.heappush(heap, (dist,next, path + [next]))



direct, distance_direct = trav(1, v)
to_friend, distance_friend = trav(1,p)
frinedToEnd, distance_friendToEnd = trav(p, v)


if not frinedToEnd:
    print("GOOD BYE")
elif distance_direct >= distance_friend + distance_friendToEnd:
    print("SAVE HIM")
else:
    print("GOOD BYE")

