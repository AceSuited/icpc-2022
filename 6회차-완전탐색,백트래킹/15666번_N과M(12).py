import sys

input = lambda:sys.stdin.readline().strip()

n,m =map(int,input().split())
seq =list(map(int,input().split()))
seq.sort()



def solve(start, depth, picked):

    if depth == m:
        print(*picked)
        return
    else:
        prev = 0
        for i in range(start, n):
            if seq[i] != prev:

                picked.append(seq[i])
                prev = seq[i]
                solve(i, depth + 1, picked)

                picked.pop()

solve(0,0,[])
