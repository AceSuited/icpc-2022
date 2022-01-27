import sys

input = lambda: sys.stdin.readline().strip()

t = int(input())
cases = []

for _ in range(t):
    n = int(input())
    cases.append(list(map(int, input().split())))

for case in cases:
    n = len(case)
    M = case[n - 1]
    cost = 0
    earn = 0
    cnt = 0
    for i in range(n - 2, -1, -1):
        if M <= case[i]:
            earn += cnt * M
            cnt = 0
            M = case[i]
        else:
            cnt += 1
            cost += case[i]

    earn += cnt * M
    print(earn - cost)
