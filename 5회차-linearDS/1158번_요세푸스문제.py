import sys

input = lambda: sys.stdin.readline().strip()
from collections import deque

n, k = map(int, input().split())

circle = deque([_ + 1 for _ in range(n )])
ans ="<"
for i in range(n):
    for j in range(k - 1):
        person = circle.popleft()
        circle.append(person)

    if i == n-1:
        ans += str(circle.popleft()) + ">"
        break
    ans += str(circle.popleft()) + ", "

print(ans)
