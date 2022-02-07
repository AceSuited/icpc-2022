import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
cases = [list(map(int,list(input()))) for _ in range(n)]


def solve(case):
    mid = len(case) // 2
    if len(case) <= 1:
        return True
    else:
        for i in range(mid):
            if case[i] == case[len(case) - i - 1]:
                return False

        return solve(case[:mid]) and solve(case[mid + 1:])


for case in cases:
    pow = 1
    if len(case) == 1:
        print("YES")
        continue
    while pow < len(case):
        pow *= 2
    if not solve(case):
        print("NO")
    else:
        print("YES")




