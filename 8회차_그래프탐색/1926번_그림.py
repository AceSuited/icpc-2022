import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]
n, m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def inRange(y,x):
    return 0<=y<n and 0<=x<m

def solve(y,x):
    queue = deque([(y,x)])
    visited[y][x] = True
    cnt = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]
            if inRange(y_,x_) and not visited[y_][x_] and board[y_][x_] == 1:
                visited[y_][x_] = True
                queue.append((y_,x_))
                cnt += 1

    return cnt

res = []
for y in range(n):
    for x in range(m):
        if board[y][x] == 1 and not visited[y][x]:
            res.append(solve(y,x))


print(len(res))


if len(res) == 0:
    print(0)
else:
    print(max(res))