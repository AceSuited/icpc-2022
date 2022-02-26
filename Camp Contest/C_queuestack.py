import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque


n = int(input())

infos = list(map(int,input().split()))
init = list(map(int,input().split()))

m = int(input())
seq = list(map(int,input().split()))

queue = deque()
for i in range(n):
    if infos[i] == 0:
        queue.append(init[i])

for i in range(m):
    queue.appendleft(seq[i])

queue.reverse()
for i in range(m):
    print(queue[i], end = " ")
