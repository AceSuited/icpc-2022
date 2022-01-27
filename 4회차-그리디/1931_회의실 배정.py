import sys
input = lambda:sys.stdin.readline()

n = int(input())

times = []
for _ in range(n):
    times.append(list(map(int,input().split())))
times.sort(key=lambda x: (x[1], x[0]))

cnt = 1
prev = times[0]
for i in range(1, n):
    if times[i][0] >= prev[1]:
        cnt += 1
        prev = times[i]

print(cnt)
