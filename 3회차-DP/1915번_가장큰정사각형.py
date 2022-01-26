import sys
input = lambda: sys.stdin.readline().strip()

n,m = map(int,input().split())
board = []

for  i in range(n):
    board.append(list(map(int,list(input()))))

for y in range(1,n):
    for x in range(1,m):
        if board[y][x] != 0:
            board[y][x] = min(board[y-1][x], board[y-1][x-1], board[y][x-1]) + 1

ans = 0
for line in board:
    ans = max(ans, max(line))

print(ans * ans)