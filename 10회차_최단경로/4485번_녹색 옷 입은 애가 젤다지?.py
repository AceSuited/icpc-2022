import heapq
import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
inf = 10000

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def inRange(y_, x_):
    return 0 <= y_ < n and 0 <= x_ < n

cnt = 1
while n != 0:
    cave = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[inf for _ in range(n)] for _ in range(n)]
    queue = []
    heapq.heappush(queue, (cave[0][0], 0, 0))
    distance[0][0] = cave[0][0]
    ans = 0
    while queue:
        current_cost, y, x = heapq.heappop(queue)
        if y == n - 1 and x == n - 1:
            ans = current_cost
            break

        visited[y][x] = True
        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]

            if inRange(y_,x_) and not visited[y_][x_] and distance[y_][x_] > current_cost + cave[y_][x_]:
                distance[y_][x_] = current_cost + cave[y_][x_]
                heapq.heappush(queue, (distance[y_][x_], y_, x_))

    ans = distance[n-1][n-1]


    print("Problem %d: %d" % (cnt,ans))
    n = int(input())
    cnt += 1