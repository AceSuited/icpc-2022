import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())

def solve(k,begin, picked, visited):
    if k == 0 :
        print(*picked)
        return
    else:
        for i in range(begin, n):
            if not visited[i]:
                picked.append(i + 1)
                visited[i] = True
                solve(k- 1, i, picked, visited)
                visited[i] = False
                picked.pop()


solve(m,0, [], [False for _ in range(n)] )