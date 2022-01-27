import sys
input = lambda:sys.stdin.readline().strip()

t = int(input())

cases = []
for _ in range(t):
    input()
    case = []
    case.append(list(input()))
    case.append(list(input()))
    cases.append(case)


for case in cases:
    n = len(case[0])
    cnt_a = case[0].count('W')
    cnt_b = case[1].count('W')


    cnt_diff= abs(cnt_a - cnt_b)
    pos_diff = 0
    for i in range(n):
        if case[0][i] != case[1][i]:
            pos_diff += 1



    print(int(cnt_diff+((pos_diff - cnt_diff) / 2)))


