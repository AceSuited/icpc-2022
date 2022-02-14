import heapq
import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))

    else:
        heapq.heappush(arr,-num)

