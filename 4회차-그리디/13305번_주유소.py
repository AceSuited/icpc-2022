import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
roads = list(map(int, input().split()))
gas = list(map(int,input().split()))

ans = 0
cheap = gas[0]
for i in range(n-1):
    if gas[i] <= cheap:
        cheap = gas[i]
    ans += roads[i] * cheap

print(ans)