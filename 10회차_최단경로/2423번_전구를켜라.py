import heapq
import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int,input().split())

def inRange(y_,x_):
    return 0<= y_ < n and 0<= x_< m


circuit = [list(input()) for _ in range(n)]
visited=  [[False for _ in range(m)] for _ in range(n )]

dy = [0,1,0,-1,-1,1,1,-1]
dx = [1,0,-1,0,-1,1,-1,1]

heap = []
if circuit[0][0] == "/":
    heapq.heappush(heap, (1,0,0))
else:
    heapq.heappush(heap,(0,0,0))

visited[0][0] = True
circuit[0][0] = "\\"

while heap:
    num_rotation, y, x = heapq.heappop(heap)
    if y == n-1 and x == m - 1 and circuit[y][x] == "\\":
        print(num_rotation)
        sys.exit()
    for i in range(8):
        y_ = y + dy[i]
        x_ = x + dx[i]
        if inRange(y_,x_):
            if visited[y_][x_]:
                continue
            else:
                if i <= 3:
                    if circuit[y_][x_] == circuit[y][x]:
                        if circuit[y][x] == "\\":
                            circuit[y_][x_] = "/"
                        elif circuit[y][x] == "/":
                            circuit[y_][x_] = "\\"
                        heapq.heappush(heap, (num_rotation + 1, y_,x_))
                        visited[y_][x_] = True
                    elif circuit[y_][x_] != circuit[y][x]:
                        heapq.heappush(heap, (num_rotation, y_, x_))
                        visited[y_][x_] = True
                elif i == 4 or i == 5:
                    if circuit[y][x] == "\\":
                        if circuit[y][x] == circuit[y_][x_]:
                            heapq.heappush(heap, (num_rotation,y_,x_))
                            visited[y_][x_] = True
                        elif circuit[y][x] != circuit[y_][x_]:
                            circuit[y_][x_] = "\\"
                            heapq.heappush(heap, (num_rotation + 1, y_,x_))
                            visited[y_][x_] = True
                elif i == 6 or i == 7:
                    if circuit[y][x] == "/":
                        if circuit[y][x] == circuit[y_][x_]:
                            heapq.heappush(heap,(num_rotation,y_,x_))
                            visited[y_][x_] = True
                        elif circuit[y][x] != circuit[y_][x_]:
                            circuit[y_][x_] = "/"
                            heapq.heappush(heap,(num_rotation+1, y_, x_))
                            visited[y_][x_] = True


print("NO SOLUTION")

