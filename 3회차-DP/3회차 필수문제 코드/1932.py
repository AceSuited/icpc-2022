import sys

n = int(sys.stdin.readline())

dp = [[0 for i in range(n+1)]]
for i in range(1, n+1):
    dp.append([0] + list(map(int, sys.stdin.readline().split())) + [0] * (n - i))


for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

ans = 0
for i in range(1, n+1):
    ans = max(ans, dp[n][i])

print(ans)