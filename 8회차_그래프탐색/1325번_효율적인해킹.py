# import sys
# input = lambda: sys.stdin.readline().strip()
# from collections import deque
#
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[v].append(u)
#
# def solve_bfs(start):
#     visited = [False] * (n + 1)
#     queue = deque([start])
#     visited[start] = True
#     cnt = 1
#     while queue:
#         current = queue.popleft()
#         for next in graph[current]:
#             if not visited[next]:
#                 queue.append(next)
#                 visited[next] = True
#                 cnt += 1
#
#     return cnt
# res = []
# for i in range(1, n + 1):
#     res.append(solve_bfs(i))
# M = max(res)
# for i in range(n):
#     if res[i] == M:
#         print(i + 1, end=" ")




##############dfs로는 메모리초과가 발생... ㅜ
import sys

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(13000)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)



def solve(cnt, current):
    visited[current] = True
    for next in graph[current]:
        if not visited[next]:
            visited[next] = True
            cnt = solve(cnt + 1, next)

    return cnt


res = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    res.append(solve(0,i))
M = max(res)
for i in range(n):
    if res[i] == M:
        print(i + 1, end=" ")




