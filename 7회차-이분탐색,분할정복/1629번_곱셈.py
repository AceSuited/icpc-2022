import sys
input =lambda:sys.stdin.readline().strip()

a,b,c = map(int,input().split())


def solve(n):

    if n == 1:
        return a % c

    temp = solve(n // 2)
    if n % 2 != 0:
        return temp * temp * a % c
    else:

        return temp * temp % c

print(solve(b) % c)