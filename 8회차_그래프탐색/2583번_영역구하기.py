import sys

input = lambda: sys.stdin.readline().strip()
from collections import deque

m, n, k = map(int, input().split())

paper = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False] * n for _ in range(m)]
squares = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for _ in range(k):
    x_0, y_0, x_1, y_1 = map(int, input().split())
    for y in range(y_0, y_1):
        for x in range(x_0, x_1):
            paper[y][x] = 1

def inRange(y,x):
    return 0<= y < m and 0 <= x < n

def trav(y,x):
    area =0
    queue = deque([])
    queue.append([y,x])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        area += 1
        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]
            if inRange(y_,x_) and not visited[y_][x_] and paper[y_][x_] == 0:
                visited[y_][x_] = True
                queue.append([y_,x_])


    return area

cnt = 0
ans = []
for y in range(m):
    for x in range(n):
        if not visited[y][x] and paper[y][x] == 0:
            ans.append(trav(y,x))
            cnt += 1

ans.sort()
print(cnt)
print(*ans)