import sys
input = lambda:sys.stdin.readline()
from collections import deque

n, k = map(int,input().split())

line = [0 for _ in range(1000000)]

visited= [False] * (1000000)
def inRange(pos):
    return 0<=pos<1000000

queue = deque([n])
visited[n] = True
while queue:
    current = queue.popleft()

    if current == k:
        break

    next = current + 1
    if inRange(next) and not visited[next]:
        visited[next] = True
        queue.append(next)
        line[next] = line[current] + 1
    next = current - 1
    if inRange(next) and not visited[next]:
        visited[next] = True
        queue.append(next)
        line[next] = line[current] + 1
    next = current * 2
    if inRange(next) and not visited[next]:
        visited[next] = True
        queue.append(next)
        line[next] = line[current] + 1

print(line[k])
