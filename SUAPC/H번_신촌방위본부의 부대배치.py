import sys
input = lambda:sys.stdin.readline().strip()
m,n,k = map(int,input().split())

soldiers = []
for i in range(k):
    x,y = map(int,input().split())
    soldiers.append((y - 1,x -1))

board_origin = [[False for _ in range(m)] for _ in range(n)]

def inRange(y_,x_):
    return 0 <= y_ < n and 0 <= x_ < m

dx = [1,0,-1,0]
dy = [0,1,0,-1]

dx_elephant = [3,2,3,2,-3,-2,-3,-2]
dy_elephant = [2,3,-2,-3,2,3,-2,-3]

attacked = [line[:] for line in board_origin]

for soldier in soldiers:
    y, x= soldier
    board_origin[y][x] = True
    for i in range(4):
        y_ = y+ dy[i]
        x_ = x + dx[i]
        if inRange(y_,x_):
            attacked[y_][x_] = True
def deploy(y,x, board):
    attacked_temp = []
    for i in range(8):
        y__ = y + dy_elephant[i]
        x__ = x + dx_elephant[i]

        if inRange(y__,x__) and board[y__][x__] == True:
            return False, []
        elif inRange(y__,x__) and board[y__][x__] == False:
            attacked_temp.append((y__,x__))
    return True, attacked_temp


ans = 0
ans_container = []

def solve(board,y,x,cnt,container):
    global ans
    global ans_container
    ans = max(cnt, ans)
    if ans == cnt:
        ans_container = container[:]
    for y_ in range(y,n):
        for x_ in range(x,m):

            if not board[y_][x_] and not attacked[y_][x_]:
                deployed, attacked_temp = deploy(y_,x_,board_origin)
                if deployed:
                    board[y_][x_] = True
                    container.append((y_,x_))
                    temp = [True for _ in range(len(attacked_temp))]
                    for i in range(len(attacked_temp)):
                        coord = attacked_temp[i]
                        if attacked[coord[0]][coord[1]] == True:
                            temp[i] = False
                        else:
                            temp[i] = True
                            attacked[coord[0]][coord[1]] = True

                    solve(board,y_,x_, cnt + 1, container)
                    for i in range(len(attacked_temp)):
                        coord = attacked_temp[i]
                        if temp[i]:
                            attacked[coord[0]][coord[1]] = False

                    container.pop()
                    board[y_][x_] = False
            if x_ == m - 1:
                x = 0


solve(board_origin, 0,0,0,[])
print(len(ans_container))
for elem in ans_container:
    y,x = elem
    print(x + 1, y + 1)