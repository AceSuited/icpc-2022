import sys

input = lambda:sys.stdin.readline().strip()

n  = int(input())
schedules = []
for _ in range(n):
    schedules.append(list(map(int,input().split())))

schedules.sort(key=lambda x: x[1], reverse=True)

current = schedules[0][1]

for i in range(n):
    if schedules[i][1] < current:
        current = schedules[i][1]

    current -= schedules[i][0]




if current >= 0:
    print(current)
else:
    print(-1)