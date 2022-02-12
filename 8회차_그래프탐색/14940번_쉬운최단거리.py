import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1 for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


visited = [[False for _ in range(m)] for _ in range(n)]

def inRange(y,x):
    return 0<= y < n and 0 <= x < m


def trav(y,x):
    queue = deque([])
    queue.append((y,x))
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            y_ = y+dy[i]
            x_ = x + dx[i]

            if inRange(y_,x_) and not visited[y_][x_] and board[y_][x_] != 0:
                visited[y_][x_] = True
                ans[y_][x_] = ans[y][x] + 1
                queue.append((y_,x_))




for y in range(n):
    for x in range(m):
        if board[y][x] == 2:
            ans[y][x] = 0
            trav(y,x)
        if board[y][x] == 0:
            ans[y][x] = 0

for line in ans:
    print(*line)