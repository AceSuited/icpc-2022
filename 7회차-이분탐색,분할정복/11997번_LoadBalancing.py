import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
coords = []
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    coords.append([x, y])

xs.sort()
ys.sort()

x_dict = {}
y_dict = {}

xs = list(set(xs))
ys = list(set(ys))
len_y = len(ys)
len_x = len(xs)

## 좌표압축
for i in range(len_x):
    x_dict[xs[i]] = i

for i in range(len_y):
    y_dict[ys[i]] = i

## 압축된 좌표로 변환
for coord in coords:
    coord[0] = x_dict[coord[0]]
    coord[1] = y_dict[coord[1]]

## 압축된 좌표로 2차원 좌표평면에 해당하는 배열 생성
board = [[0 for _ in range(len_x)] for _ in range(len_y)]
for coord in coords:
    board[coord[1]][coord[0]] = 1

## 부분합 배열 생성
board_sum = [[0 for _ in range(len_x + 1)] for _ in range(len_y + 1)]
for y in range(len_y):
    for x in range(len_x):
        board_sum[y + 1][x + 1] = sum(board[y][:x + 1])

for x in range(len_x + 1):
    for y in range(len_y):
        board_sum[y + 1][x] += board_sum[y][x]

def range_sum(y, x, y_, x_):
    temp = board_sum[y_][x_] - board_sum[y_][x] - board_sum[y][x_] + board_sum[y][x]
    return temp

## 결과계산
ans = n
for y in range(1, len_y + 1):
    for x in range(1, len_x + 1):
        temp = max(range_sum(0,0,y,x), range_sum(y, 0, len_y, x), range_sum(y, x, len_y, len_x),
                   range_sum(0, x, y, len_x))
        ans = min(ans, temp)

print(ans)
