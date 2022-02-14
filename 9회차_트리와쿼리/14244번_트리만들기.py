import sys
input = lambda:sys.stdin.readline().strip()
n, m = map(int,input().split())

for i in range(0, n - m):
    print(i, i + 1)
for j in range(i + 2, n):
    print(i + 1, j)

