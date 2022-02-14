import sys
input = lambda:sys.stdin.readline().strip()
n,p,q,x,y = map(int,input().split())


dic = dict()
dic[0] = 1
dic[1] = 2
def solve(n):
    if n <= 0:
        return 1
    else:
        if n in dic:
            return dic[n]
        else:
            term_a, term_b = (n // p) - x, (n //q) - y

            dic[n] = solve(term_a) + solve(term_b)
            return dic[n]

print(solve(n))