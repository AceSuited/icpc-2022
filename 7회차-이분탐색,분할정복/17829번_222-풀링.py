import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def pooling(board):
    board.sort()
    return board[-2]

def merge(board_1, board_2, board_3, board_4):
    res = []
    res.append(pooling(board_1))
    res.append(pooling(board_2))
    res.append(pooling(board_3))
    res.append(pooling(board_4))

    return res

def divide(board, length):
    if length == 2:
        two_by_two = []
        for line in board:
            for e in line:
                two_by_two.append(e)
        return two_by_two

    temp_1 = []
    for y in range(length // 2):
        temp = []
        for x in range(length // 2):
            temp.append(board[y][x])
        temp_1.append(temp)
    temp_2 = []
    for y in range(length // 2):
        temp = []
        for x in range(length // 2, length):
            temp.append(board[y][x])
        temp_2.append(temp)
    temp_3 = []
    for y in range(length // 2, length):
        temp=[]
        for x in range(length // 2):
            temp.append(board[y][x])
        temp_3.append(temp)
    temp_4 = []
    for y in range(length // 2, length):
        temp=[]
        for x in range(length // 2, length):
            temp.append(board[y][x])
        temp_4.append(temp)

    return merge(divide(temp_1,length // 2),divide(temp_2,length//2),divide(temp_3,length//2),divide(temp_4,length//2))

res = pooling(divide(board,n))
print(res)