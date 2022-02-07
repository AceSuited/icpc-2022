import sys
input = lambda:sys.stdin.readline().strip()

x, y, a_0, a_1, n = map(int,input().split())

W = [[x,y], [1,0]]
V = [[a_1], [a_0]]

def mult_res(W, V):
    res = [[0],[0]]
    for i in range(2):
        for j in range(2):
            res[i][0] += (W[i][j] * V[j][0]) % 100
    return res

def square_W(A, B):
    res = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += (A[i][k] * B[k][j]) % 100
    return res


def solve(n):
    if n == 1:
        return W
    else:
        temp = solve(n//2)
        if n % 2 == 0:
            return square_W(temp, temp)
        else:
            return square_W(W, square_W(temp, temp))


if n == 0:
    print("%.2d" % (a_0))
    sys.exit()
elif n == 1:
    print("%.2d" % (a_1))
    sys.exit()
else:

    ans = mult_res(solve(n-1), V)
    print("%.2d" % (ans[0][0] % 100))