import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())

trees = list(map(int,input().split()))

trees.sort(reverse=True)
remain = 0
time = 1

for i in range(n):
    remain -= 1
    time += 1
    remain = max(remain, trees[i])

while remain > 0 :
    remain -= 1
    time += 1


print(time)