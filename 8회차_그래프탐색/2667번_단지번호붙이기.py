import sys

input = lambda: sys.stdin.readline().strip()
from collections import deque

n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]

ans = []
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def inRange(y, x):
    return 0 <= y < n and 0 <= x < n


def solve(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]
            if inRange(y_, x_) and not visited[y_][x_] and board[y_][x_] == 1:
                visited[y_][x_] = True
                queue.append((y_, x_))

                cnt += 1

    return cnt


for sero in range(n):
    for garo in range(n):
        if not visited[sero][garo] and board[sero][garo] == 1:
            ans.append(solve(sero, garo))

ans.sort()
print(len(ans))
for _ in range(len(ans)):
    print(ans[_])
