import sys
input = lambda:sys.stdin.readline()
from collections import deque

n = int(input())
cases = [list(map(int,input().split())) for _ in range(n)]

primes = [True for _ in range(10000)]

for i in range(2,10000):
    if primes[i]:
        current = primes[i]
    else:
        continue

    idx = 2
    while i * idx < 10000:
        primes[i * idx] = False
        idx += 1


for case in cases:
    visited = [-1 for _ in range(10000)]
    queue = deque([case[0]])
    visited[case[0]] = 0
    ans = -1
    while queue:
        current = queue.popleft()
        if current == case[1]:
            ans = visited[case[1]]
            break
        else:
            for i in range(4):
                next = list(map(int, list(str(current))))
                if i == 0:
                    start = 1
                else:
                    start = 0
                for j in range(start,10):
                    next[i] = j
                    next_ = next[0] * 1000 + next[1] * 100 + next[2] * 10 + next[3]
                    if visited[next_] == -1 and primes[next_]:
                        visited[next_] = visited[current] + 1
                        queue.append(next_)


    if ans == -1:
        print("Impossible")
    else:
        print(ans)