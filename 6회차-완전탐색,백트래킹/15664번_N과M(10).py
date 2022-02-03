import sys
input = lambda:sys.stdin.readline().strip()
n, m = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()
visited = [False] * n

def solve(start,depth, picked):
    if depth == m:
        print(*picked)
    else:
        prev = -1
        for i in range(start, n):

            if not visited[i] and seq[i] != prev:
                picked.append(seq[i])
                visited[i] = True
                prev = seq[i]
                solve(i, depth + 1, picked)
                visited[i] = False
                picked.pop()

solve(0,0,[])


