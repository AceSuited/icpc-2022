import sys
input = lambda:sys.stdin.readline().strip()
from itertools import permutations

n = int(input())
sequence = list(map(int,input().split()))

perm = permutations(sequence,n)

def calculate(seq):

    result = 0
    for i in range(0, len(seq) - 1):
        result += abs(seq[i] - seq[i+1])
    return result


visited = [False] * n

ans = -1099000000000000
def solve(depth,picked):
    global ans
    if depth == n:
        ans = max(calculate(picked), ans)
    else:
        for i in range(n):
            if not visited[i]:
                picked.append(sequence[i])
                visited[i] = True
                solve(depth + 1, picked)
                visited[i] = False
                picked.pop()


for seq in perm:
    ans = max(calculate(seq),ans)

# solve(0,[])
print(ans)