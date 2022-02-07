import copy
import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n = int(input())
graph = [[] for _ in range(n + 1)]
inputs = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
origins = list(map(int, input().split()))
for i in range(len(inputs)):
    info = inputs[i]
    for j in range(len(info) - 1):
        graph[i + 1].append(info[j])

time = [-1] * (n + 1)
visited = [0] * (n + 1)
rumored = [False] * (n+1)
for origin in origins:
    time[origin] = 0
    rumored[origin] = True

queue = deque(origins)

while queue:
    current = queue.popleft()

    for next in graph[current]:
        if rumored[next]:
            continue
        visited[next] += 1
        if visited[next] * 2 >= len(graph[next]):
            queue.append(next)
            time[next] = time[current] + 1
            rumored[next] = True

print(*time[1:])
