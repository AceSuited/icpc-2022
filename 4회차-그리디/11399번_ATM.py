import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())

times = list(map(int,input().split()))

times.sort()
result = 0
for i in range(n):
    for j in range(i + 1):
        result += times[j]
print(result)