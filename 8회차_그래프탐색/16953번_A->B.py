import sys
input = lambda:sys.stdin.readline().strip()

a, b = map(int,input().split())

ans = -1
def solve(cnt, current):
    global ans
    if current > b:
        return -1
    if current == b:
        ans = cnt + 1
        return cnt + 1
    solve(cnt + 1, int(str(current) + "1"))
    solve(cnt + 1, current * 2)

solve(0, a)
print(ans)