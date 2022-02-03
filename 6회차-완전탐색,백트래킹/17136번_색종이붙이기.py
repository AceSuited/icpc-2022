import copy
import sys

input = lambda: sys.stdin.readline().strip()
board_origin = []

ones_init = 0

for _ in range(10):
    line = list(map(int,input().split()))
    board_origin.append(line)
    ones_init += line.count(1)

container = [5, 5, 5, 5, 5]


def inRange(y, x):
    if 0 <= y <= 10 and 0 <= x <= 10:
        return True
    return False

def check(board, y_start, x_start, size):
    if not inRange(y_start + size, x_start + size):
        return False
    for y in range(y_start, y_start + size):
        for x in range(x_start, x_start + size):
            if board[y][x] == 0:
                return False

    return True

def color(board, y_start, x_start, size):
    for y in range(y_start, y_start + size):
        for x in range(x_start, x_start + size):
            board[y][x] = 0

def erase(board, y_start, x_start, size):
    for y in range(y_start, y_start + size):
        for x in range(x_start, x_start + size):
            board[y][x] = 1
ans = 1000000
def solve(board, cnt, deleted):
    # for line in board:
    #     print(line)
    # print("----------------------------", deleted)
    global ans
    if deleted == ones_init:
        ans = min(cnt, ans)
        return

    for y in range(10):
        for x in range(10):
            if board[y][x] == 1:
                for size in range(5, 0, -1):
                    if check(board, y,x,size) and container[size - 1] > 0:
                        color(board,y,x,size)
                        container[size - 1] -= 1
                        cnt += 1
                        solve(board, cnt, deleted + (size * size))
                        cnt -= 1
                        erase(board,y,x,size)
                        container[size-1] += 1
                return

solve(board_origin,0,0)
if ans == 1000000:
    print(-1)
else:
    print(ans)
