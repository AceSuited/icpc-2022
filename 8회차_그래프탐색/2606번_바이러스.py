import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque
n = int(input())
m = int(input())
graph = [[]for _ in range(n + 1)]
visited= [False] * (n + 1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque([1])
visited[1] = True
cnt = 0
while que:
    current = que.popleft()
    for next in graph[current]:
        if not visited[next]:
            visited[next] = True
            que.append(next)
            cnt += 1

print(cnt)