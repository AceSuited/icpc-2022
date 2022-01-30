# python3으로 통과하려면 최적화가 필요하다고 합니다
# pypy3으로 제출
import sys

n = int(sys.stdin.readline())
dp = [[-1 for _ in range(505)] for _ in range(505)]
a = []
b = []

def solve(s, e):
    if dp[s][e] != -1:
        print("@!")
        return dp[s][e]

    if s == e:
        dp[s][e] = 0
        return dp[s][e]
    
    dp[s][e] = 987654321
    for i in range(s, e):
        dp[s][e] = min(dp[s][e], a[s] * b[i] * b[e] + solve(s, i) + solve(i + 1, e))

    return dp[s][e]



for i in range(n):
    at, bt = map(int, sys.stdin.readline().split())
    a.append(at)
    b.append(bt)
    
print(solve(0, n-1))