import sys
input = lambda:sys.stdin.readline().strip()

n, k = map(int,input().split())

mem = [[0,1], [1,1]]

for i in range(2,1001):
    cont = []
    for j in range(i + 1):

        if j == 0:
            cont.append(1)
        elif j == i:
            cont.append(1)
        else:
            cont.append(mem[i-1][j-1] + mem[i-1][j])
    mem.append(cont)

print(mem[n][k] % 10007)