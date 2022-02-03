import sys
input = lambda:sys.stdin.readline().strip()
from itertools import combinations

ans = []
seq =input()
if len(seq) < 10:
    nums = len(seq)
elif len(seq) == 10:
    nums = 10
else:
    nums = (len(seq) - 9) // 2 + 9

visited = [False for _ in range(nums)]

def solve(index,depth, picked):
    # print(index, depth, picked)
    if index == len(seq):
        print(*picked)
        sys.exit()
    if index + 1 <= len(seq):
        if int(seq[index:index+1]) <= nums and not visited[int(seq[index:index+1]) -1]:
            picked.append(seq[index:index+1])
            visited[int(seq[index:index + 1]) - 1] = True
            solve(index + 1, depth + 1, picked)
            visited[int(seq[index:index + 1]) - 1] = False
            picked.pop()
    if index + 2 <= len(seq):
        if int(seq[index:index+2]) <= nums and not visited[int(seq[index:index+2]) -1]:
            picked.append(seq[index:index+2])
            visited[int(seq[index:index+2])- 1] = True
            solve(index+2, depth + 1, picked)
            visited[int(seq[index:index + 2]) - 1] = False
            picked.pop()

solve(0,0,[])