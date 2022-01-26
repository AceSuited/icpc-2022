import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(n)]

mem = [[0 for _ in range(m)] for _ in range(n)]
mem[0][0] = maze[0][0]
for y in range(n):
    for x in range(m):
        if y == 0 and x == 0:
            continue
        if y == 0:
            mem[y][x] = maze[y][x] + mem[y][x-1]
        elif x == 0:
            mem[y][x] = maze[y][x] + mem[y-1][x]
        else:
            mem[y][x] = max(maze[y][x] + mem[y-1][x], maze[y][x] + mem[y][x-1], maze[y][x] + mem[y-1][x - 1])


print(mem[n-1][m-1])