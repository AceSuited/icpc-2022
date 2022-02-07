import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
board = [list(map(int,list(input()))) for _ in range(n)]

ans = ""

def solve(y,x, isEnd, leng):
    global ans
    if leng == 1:
        ans += str(board[y][x])

    else:
        color = board[y][x]
        possible = True
        for y_ in range(y, y + leng):
            for x_ in range(x, x+leng):
                if color != board[y_][x_]:
                    possible = False
                    break

            if not possible:
                break

        if possible:
            ans += str(color)
        else:
            half = leng // 2
            ans += "("
            solve(y,x, False,half)
            solve(y, x+half,False, half)
            solve(y + half, x, False, half)
            solve(y+half,x+ half, True, half)

    if isEnd:
        ans += ")"


solve(0,0,False,n)
print(ans)