import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
weights = list(map(int,input().split()))

weights.sort()

if weights[0] != 1:
    print(1)
    sys.exit()

sum = 1

for i in range(1,n):
    if weights[i] > sum + 1:
        print(sum+1)
        exit()

    sum += weights[i]

print(sum + 1)