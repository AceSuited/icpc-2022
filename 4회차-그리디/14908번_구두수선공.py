import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
work_time = []
work_cost = []
works =[]
for _ in range(n):
    init = list(map(int,input().split()))
    init.append(_ + 1)
    works.append(init)



ans = []
days = 0
while len(works) > 1:
    if works[-1][1] * works[-2][0] > works[-2][1] * works[-1][0]:
        current = works.pop()
        ans.append(current[2])
    elif works[-1][1] * works[-2][0] == works[-2][1] * works[-1][0]:
        if works[-1][2] < works[-2][2]:
            current = works.pop()
            ans.append(current[2])
        else:
            works[-1],works[-2] = works[-2],works[-1]
    else:
        works[-1], works[-2] = works[-2], works[-1]


ans.append(works[0][2])
print(*ans)