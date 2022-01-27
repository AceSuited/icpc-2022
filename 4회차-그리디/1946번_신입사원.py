import sys
input = lambda: sys.stdin.readline().strip()

cases = []
t = int(input())

for i in range(t):
    n = int(input())
    grades = []
    for _ in range(n):
        grades.append(list(map(int,input().split())))

    cases.append(grades)



for case in cases:

    n = len(case)
    case.sort(key=lambda x : x[0])

    cnt = 1
    min_rank = case[0][1]

    for i in range(n):
        if case[i][1] < min_rank:
            min_rank = case[i][1]
            cnt += 1
    print(cnt)