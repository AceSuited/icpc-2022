import sys

input = lambda: sys.stdin.readline().strip()

t = int(input())
inf = 10e6


for _ in range(t):

    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [inf for _ in range(n + 1)]

    for i in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for i in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e,-t))

    for i in range(n + 1):
        graph[0].append((i, 1))
        graph[i].append((0, 1))

    distance[0] = 0

    isNegative = False

    for iter in range(n):
        for current in range(1, n + 1):
            for next, cost in graph[current]:
                if distance[next] > distance[current] + cost:
                    distance[next] = distance[current] + cost
                    if iter == n - 1:
                        isNegative = True

    if isNegative:
        print("YES")
    else:
        print("NO")