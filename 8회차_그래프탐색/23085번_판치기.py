import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

n, k = map(int, input().split())
coins = list(input())
visited = dict()

init = coins.count("T")

queue = deque([init])
visited[init] = 0
ans = -1
while queue:
    current_t = queue.popleft()
    current_h = n - current_t
    if current_t == n:
        ans = visited[current_t]
        break
    else:
        for i in range(k):
            turn_t = i
            turn_h = k - i

            if turn_t <= current_t and turn_h <= current_h:
                next_t = current_t + turn_h - turn_t
                if next_t not in visited:
                    visited[next_t] = visited[current_t] + 1
                    queue.append(next_t)

print(ans)
