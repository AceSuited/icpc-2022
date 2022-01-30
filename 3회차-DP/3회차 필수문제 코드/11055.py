import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(1001)]

ans = 0
for it in a:
    dp[it] = it
    dp[it] += max(dp[:it])
    ans = max(ans, dp[it])
    
print(ans)
