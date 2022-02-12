import sys

input = lambda: sys.stdin.readline()
from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

queue = deque([])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def inRange(y, x):
    return 0 <= y < n and 0 <= x < m


def solve(queue):

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]
            if inRange(y_,x_) and visited[y_][x_] == -1 and board[y_][x_] == 0:
                board[y_][x_] = 1
                visited[y_][x_] = visited[y][x] + 1
                queue.append((y_,x_))



for y in range(n):
    for x in range(m):
        if board[y][x] == 1 and visited[y][x] == -1:
            queue.append((y, x))
            visited[y][x] = 0
cnt = solve(queue)

day = -1
for y in range(n):
    for x in range(m):
        if visited[y][x] == -1 and board[y][x] == 0:
            print(-1)
            sys.exit()
        day = max(day, visited[y][x])
print(day)