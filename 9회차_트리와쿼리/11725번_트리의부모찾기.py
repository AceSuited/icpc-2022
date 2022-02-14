import sys
input = lambda:sys.stdin.readline().strip()
sys.setrecursionlimit(10**5)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n - 1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=  [False for _ in range(n + 1)]
parent = [-1 for _ in range(n+1)]
def trav(current):


    for next in graph[current]:
        if not visited[next]:
            visited[next] = True
            parent[next] = current
            trav(next)
    return


trav(1)
for i in range(2, n + 1):
    print(parent[i])
