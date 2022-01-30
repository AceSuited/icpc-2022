import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n, k, m = map(int, input().split())

circle = deque([_ + 1 for _ in range(n)])

cnt = m
for i in range(n):
    for j in range(k - 1):
        person = circle.popleft()
        circle.append(person)

    print(circle.popleft())
    cnt -= 1

    if cnt == 0:
        circle.reverse()
        cnt = m
