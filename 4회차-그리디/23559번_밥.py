import sys
input = lambda:sys.stdin.readline().strip()

n, x = map(int,input().split())


costs =[]
for _ in range(n):
    costs.append(list(map(int,input().split())))

costs.sort(key = lambda x: x[1] - x[0])

ans = 0

for i in range(n):
    if x - 5000 >=(n - i - 1 ) * 1000 and costs[i][0]> costs[i][1]:
        ans += costs[i][0]
        x -= 5000
    else:
        ans += costs[i][1]
        x -= 1000

print(ans)