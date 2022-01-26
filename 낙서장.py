import sys
input = lambda:sys.stdin.readline().strip()

t = int(input())
cases = []
for _ in range(t):
    case = []
    n = int(input())
    for _ in range(n):
        case.append((input()))

    case.sort()
    cases.append(case)
for case in cases:
    flag = True
    for i in range(len(case) - 1):
        if  case[i] == case[i + 1][:len(case[i])]:

            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")