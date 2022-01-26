import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

ans = triangle[0][0]

for y in range(1, n):
    for x in range(len(triangle[y])):
        if x == 0:
            triangle[y][x] += triangle[y - 1][x]
        elif x == len(triangle[y]) - 1:
            triangle[y][x] += triangle[y - 1][x - 1]
        else:
            triangle[y][x] += max(triangle[y - 1][x - 1], triangle[y - 1][x])

print(max(triangle[len(triangle) - 1]))
