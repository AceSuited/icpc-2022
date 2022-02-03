import sys
input = lambda:sys.stdin.readline().strip()

n,m = map(int, input().split())

def solve(start, depth, picked):
    if depth == m:
        print(*picked)
    else:
        for i in range(start, n):
            picked.append(i+1)
            solve(i, depth + 1, picked)
            picked.pop()

solve(0,0,[])