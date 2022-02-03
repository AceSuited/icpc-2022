import sys
input = lambda:sys.stdin.readline().strip()

n,m = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()
visited = [False for _ in range(n)]
def solve(depth, picked):
    if depth == m:
        print(*picked)
    else:
        for i in range(n):
            if not visited[i]:
                picked.append(seq[i])
                visited[i] = True
                solve(depth + 1 , picked)
                picked.pop()
                visited[i] = False

solve(0,[])