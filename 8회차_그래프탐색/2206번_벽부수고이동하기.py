import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque


n,m = map(int,input().split())

board =[list(map(int,list(input()))) for _ in range(n)]
visited = [[[-1,-1] for _ in range(m)] for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def inRange(y,x):
    return 0<=y<n and 0<=x<m

cand = []
visited[0][0][0] = 1
def search(y,x,  visited):
    queue = deque([(y,x, False)])
    while queue:
        y, x, destroyed = queue.popleft()
        for i in range(4):
            y_ = y+dy[i]
            x_ = x+dx[i]
            if not destroyed:
                if inRange(y_,x_) and board[y_][x_] == 0 and visited[y_][x_][0] == -1:
                    visited[y_][x_][0] = visited[y][x][0] + 1
                    queue.append((y_,x_, False))
                elif inRange(y_,x_) and board[y_][x_] == 1 and visited[y_][x_][1] == -1:
                    visited[y_][x_][1] = visited[y][x][0] + 1
                    queue.append((y_, x_, True))
            else:
                if inRange(y_, x_) and board[y_][x_] == 0 and visited[y_][x_][1] == -1:
                    visited[y_][x_][1] = visited[y][x][1] + 1
                    queue.append((y_, x_, True))


    return visited[n-1][m-1]

res = (search(0,0,visited))

for line in visited:
    print(line)
if res[0] == -1 and res[1] == -1:
    print(-1)
elif -1 in res:
    res.remove(-1)
    print(res[0])
else:
    print(min(res))

