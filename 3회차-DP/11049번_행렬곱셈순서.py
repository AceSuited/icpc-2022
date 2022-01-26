import sys
input = lambda :sys.stdin.readline().strip()


n = int(input())

matrixes = []

mem = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    matrixes.append(list(map(int,input().split())))


for d in range(1,n):
    for i in range(n - d):

        if d == 1:
            mem[i][i+d] = matrixes[i][0] * matrixes[i][1] * matrixes[d + i][1]
        else:

            mem[i][i + d] = 2 ** 32
            for k in range(i, i + d):
                mem[i][i+d] = min(mem[i][i+d], mem[i][k] + mem[k + 1][i + d] + matrixes[i][0] * matrixes[k][1] * matrixes[i+d][1])


print(mem[0][n-1])