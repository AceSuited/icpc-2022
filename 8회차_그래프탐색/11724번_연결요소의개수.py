import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def solve(current):
    visited[current] = True
    for next in graph[current]:
        if not visited[next]:
            visited[next] = True
            solve(next)




cnt = 0
for i in range(1,n + 1):
    if not visited[i]:
        solve(i)
        cnt += 1

print(cnt)