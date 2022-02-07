import sys
input = lambda:sys.stdin.readline().strip()

posters = []

coords_set = set()
coords_dict = {}
n = int(input())
for _ in range(n):
    start, end = map(int,input().split())
    coords_set.add(start)
    coords_set.add(end)
    posters.append([start,end])


coords = list(coords_set)
coords.sort()

for i in range(len(coords)):
    coords_dict[coords[i]] = i

for i in range(n):
    posters[i] = [coords_dict[posters[i][0]], coords_dict[posters[i][1]]]

board = [-1 for i in range(coords_dict[coords[-1]] + 1)]
for i in range(n):

    start, end = posters[i]

    for j in range(start, end+1):
        board[j] = i

board = set(board)
if -1 in board:
    ans = len(board) - 1
else:
    ans = len(board)
print(ans)
