import sys

input = lambda: sys.stdin.readline().strip()
from collections import deque

n = int(input())
picture = [list(input()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False for _ in range(n)] for _ in range(n)]

def inRange(y, x):
    return 0 <= y < n and 0 <= x < n

def solve(y, x, color):
    queue = deque([])
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]
            if inRange(y_, x_) and not visited[y_][x_] and picture[y_][x_] in color:
                queue.append((y_, x_))
                visited[y_][x_] = True


cnt_red = 0
cnt_green = 0
cnt_blue = 0
cnt_red_green = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x] and picture[y][x] == "R":
            solve(y, x, ["R"])
            cnt_red += 1
        elif not visited[y][x] and picture[y][x] == "G":
            solve(y, x, ["G"])
            cnt_green += 1
        elif not visited[y][x] and picture[y][x] == "B":
            solve(y, x, ["B"])
            cnt_blue += 1

visited = [[False for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        if not visited[y][x] and (picture[y][x] == "R" or picture[y][x] == "G"):
            solve(y, x, ["R", "G"])
            cnt_red_green += 1

print(cnt_green + cnt_blue + cnt_red, cnt_red_green + cnt_blue)
