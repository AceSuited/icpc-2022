import sys

input = lambda: sys.stdin.readline().strip()
from collections import deque

n, m = map(int, input().split())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def inRange(y_, x_):
    return 0 <= y_ < n and 0 <= x_ < m


villages = [list(map(int, input().split())) for _ in range(n)]
visited_a = [[-1 for _ in range(m)] for _ in range(n)]
visited_b = [[-1 for _ in range(m)] for _ in range(n)]
villages_res = [[-1 for _ in range(m)] for _ in range(n)]

queue = deque([])
res = [0, 0, 0, 0]
for y in range(n):
    for x in range(m):
        if villages[y][x] == 1:
            queue.append((y, x, 1))
            visited_a[y][x] = 1
            villages_res[y][x] = 1

        elif villages[y][x] == 2:
            queue.append((y, x, 2))
            visited_b[y][x] = 1
            villages_res[y][x] = 2

while queue:

    y, x, type = queue.popleft()
    if villages_res[y][x] == 3:
        res[3] += 1
        continue
    if type == 1:
        visited = visited_a
        visited_other = visited_b
    elif type == 2:
        visited = visited_b
        visited_other = visited_a
    res[type] += 1
    for i in range(4):
        y_ = y + dy[i]
        x_ = x + dx[i]

        if inRange(y_, x_) and villages[y_][x_] == 0 and visited[y_][x_] == -1:
            if visited_other[y_][x_] != -1:
                if visited_other[y_][x_] == visited[y][x] + 1:
                    villages_res[y_][x_] = 3
                    visited[y_][x_] = visited[y][x] + 1
            else:
                visited[y_][x_] = visited[y][x] + 1
                villages_res[y_][x_] = type
                queue.append((y_, x_, type))

for i in range(1, 4):
    print(res[i], end=" ")
