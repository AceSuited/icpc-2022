import sys

input = lambda: sys.stdin.readline().strip()
from collections import deque

temp = 0

n = int(input())


def inRange(y, x):
    return 0 <= y < n and 0 <= x < n


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

board = [list(input()) for _ in range(n)]
print(board)

visited = [[False for _ in range(n)] for _ in range(n)]
visited[0][0] = True
visited[n - 1][n - 1] = True

index = 1
def mark_block(y,x, type):
    global index
    queue = deque([])
    queue.append((y,x))
    visited[y][x] = True
    board[y][x] = index
    cnt= 0
    while queue:
        y, x = queue.popleft()
        cnt += 1
        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]

            if inRange(y_,x_ ) and not visited[y_][x_] :
                if board[y_][x_] == type:
                    visited[y_][x_] = True
                    queue.append((y_,x_))
                    board[y_][x_] = index
    return cnt
def find_neighbor(y,x, type):
    queue = deque([])
    queue.append((y,x))
    visited[y][x] = True
    neighbor = set()
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]

            if inRange(y_,x_ ) and not visited[y_][x_] :
                if board[y_][x_] == type:
                    visited[y_][x_] = True
                    queue.append((y_,x_))
                    board[y_][x_] = index
                else:
                    neighbor.add(board[y_][x_])
    return neighbor



table = dict()

idx = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            cnt = mark_block(y,x,board[y][x])
            table[index] = cnt
            index += 1


for line in board:
    print(line)

visited = [[False for _ in range(n)] for _ in range(n)]
visited[0][0] = True
visited[n - 1][n - 1] = True

graph = [[] for i in range(index + 1)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            neighbors = list(find_neighbor(y, x, board[y][x]))
            for i in range(len(neighbors)):
                graph[board[y][x]].append(neighbors[i])
                graph[neighbors[i]].append(board[y][x])

print(graph)
print(table)