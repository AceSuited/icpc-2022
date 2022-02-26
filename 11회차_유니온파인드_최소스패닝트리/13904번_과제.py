# import heapq
# import sys
# input = lambda:sys.stdin.readline().strip()
#
# n = int(input())
#
# tareas = []
# times = set()
# for _ in range(n):
#     t, value = map(int, input().split())
#     tareas.append((t,value))
#     times.add(t)
# tareas.sort(key = lambda x: (x[0],x[1]))
# times = list(times)
# times.sort(reverse=True)
#
# cand = []
# ans = 0
# for time in range(max(times), 0, -1):
#
#     while tareas and tareas[-1][0] == time:
#         tarea = tareas.pop()
#         heapq.heappush(cand, (-tarea[1], tarea[1] ))
#
#     if cand:
#         ans += heapq.heappop(cand)[1]
#
# print(ans)


##유니온파인드 풀이

import heapq
import sys
input = lambda:sys.stdin.readline().strip()
# sys.setrecursionlimit(10**5)
n = int(input())

tareas = []
times = []
for _ in range(n):
    t, value = map(int, input().split())
    tareas.append((t,value))
    times.append(t)


roots = [i for i in range(max(times) + 1)]
schedule = [-1 for _ in range(max(times) + 1)]

tareas.sort(key=  lambda x: x[1], reverse= True)

def find(x):
    if x == roots[x]:
        return x

    roots[x] = find(roots[x])
    return roots[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    roots[x] = y


for tarea in tareas:
    t, cost = tarea
    day = find(t)
    if schedule[day] == -1:
        schedule[day] = cost
    if day - 1 > 0:
        union(day,day - 1)

ans = 0
for val in schedule:
    if val != -1:
        ans += val

print(ans)