import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int,input().split())

visited = [False for _ in range(n)]

def solve(depth, container):
    if depth == m:
        print(*container)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            container.append(i+1)
            solve(depth + 1, container)

            visited[i] = False
            container.pop()

solve(0, [])
