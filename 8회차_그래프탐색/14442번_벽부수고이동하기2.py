import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque


n,m, k = map(int,input().split())

board =[list(map(int,list(input()))) for _ in range(n)]
visited = [[[-1 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def inRange(y,x):
    return 0<=y<n and 0<=x<m

cand = []
visited[0][0][0] = 1
def search(y,x,  visited):
    queue = deque([(y,x, 0)])
    while queue:
        y, x, destroyed = queue.popleft()
        for i in range(4):
            y_ = y+dy[i]
            x_ = x+dx[i]

            if inRange(y_,x_) and board[y_][x_] == 0 and visited[y_][x_][destroyed] == -1:
                visited[y_][x_][destroyed] = visited[y][x][destroyed] + 1
                queue.append((y_,x_, destroyed))
            elif inRange(y_,x_) and board[y_][x_] == 1 and destroyed + 1 < k + 1 and visited[y_][x_][destroyed + 1] == -1:
                visited[y_][x_][destroyed + 1] = visited[y][x][destroyed] + 1
                queue.append((y_, x_, destroyed + 1))


    return visited[n-1][m-1]

res = (search(0,0,visited))


found = False
for i in range(k + 1):
    if res[i] != -1:
        found = True

if not found:
    print(-1)
else:
    if -1 in res:
        res = list(set(res))
        res.remove(-1)
        print(min(res))
    else:
        print(min(res))

