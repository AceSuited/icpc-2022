import sys
input = lambda:sys.stdin.readline().strip()

n, k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

cnt = 0
current = k + 1
while k != 0:

    while current > k:
        current = coins.pop()
    k -= current
    cnt += 1
print(cnt)