import sys

input = lambda: sys.stdin.readline().strip()
from collections import deque

n, m, t = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
tracker = [[-1] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

gram = ()


def inRange(y, x):
    return 0 <= y < n and 0 <= x < m


def trav():
    ans = 200000
    queue = deque([(0, 0)])
    visited[0][0] = True
    tracker[0][0] = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]

            if inRange(y_, x_) and not visited[y_][x_]:
                if maze[y_][x_] != 1:
                    visited[y_][x_] = True
                    queue.append((y_, x_))
                    tracker[y_][x_] = tracker[y][x] + 1
                    if maze[y_][x_] == 2:
                        ans = (tracker[y_][x_]) + (n - y_ - 1) + (m - x_ - 1)

    if tracker[n-1][m-1] == -1:
        return ans
    return min(tracker[n-1][m-1], ans)

time = trav()
if time > t or time == -1:
    print("Fail")
else:
    print(time)