import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque

n, m = map(int,input().split())
islands = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    islands[a].append((b,c))
    islands[b].append((a,c))
s, e = map(int,input().split())

def calculate(chocos):
    visited = [False for _ in range(n + 1)]
    queue = deque([s])
    visited[s] = True
    while queue:
        current = queue.popleft()
        if current == e:
            return True
        for next in islands[current]:
            if not visited[next[0]] and next[1] >= chocos:
                visited[next[0]] = True
                queue.append(next[0])

    return False

def search():
    start = 0
    end = 1000000000
    ret = 0
    while start <= end:
        half = (start + end) // 2
        if calculate(half):
            start = half + 1
            ret = half
        else:
            end = half - 1

    return ret

print(search())
