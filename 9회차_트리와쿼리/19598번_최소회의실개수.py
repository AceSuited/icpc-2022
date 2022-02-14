import sys
input = lambda:sys.stdin.readline().strip()
import heapq

n = int(input())
schedule = []
for _ in range(n):
    start, end = map(int,input().split())
    schedule.append([start,end])

schedule.sort(key= lambda x: x[0])

rooms = [0]
ans = 1
for conf in schedule:
    start, end = conf
    if start >= rooms[0]:
        heapq.heappop(rooms)
    else:
        ans += 1

print(ans)