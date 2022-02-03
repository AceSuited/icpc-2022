import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int,input().split())
board= [list(input())for _ in range(n)]

nexter = {"W" : "B", "B": "W"}

ans = 10000000000000000
for y_ in range(n - 7):
    for x_ in range(m - 7):

        cnt = 0
        prev = board[y_][x_]
        for y in range(y_,y_+8):
            prev = nexter[prev]
            for x in range(x_ ,x_+8):
                if board[y][x] != nexter[prev]:
                    cnt += 1
                prev = nexter[prev]

        ans = min(ans, cnt)

        cnt = 0
        prev = nexter[board[y_][x_]]
        for y in range(y_,y_+8):
            prev = nexter[prev]
            for x in range(x_ ,x_+8):
                if board[y][x] != nexter[prev]:
                    cnt += 1
                prev = nexter[prev]

        ans = min(ans, cnt)

print(ans)
