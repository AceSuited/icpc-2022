import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

cnt_blue = 0
cnt_white = 0
def solve(y, x, leng):

    global cnt_white, cnt_blue
    if leng == 1:
        if board[y][x]:
            cnt_blue += 1
        else:
            cnt_white += 1
        return

    else:
        isPiece = True
        color = board[y][x]
        for y_ in range(y, y+ leng):
            for x_ in range(x, x+leng):
                if color != board[y_][x_]:
                    isPiece = False
                    break
            if not isPiece:
                break
        if isPiece:
            if color:
                cnt_blue += 1
            else:
                cnt_white += 1
            return
        else:
            half = leng // 2
            solve(y,x, half)
            solve(y, x+half, half)
            solve(y+half, x+half, half)
            solve(y+half, x, half)
solve(0,0,n)

print(cnt_white)
print(cnt_blue)


