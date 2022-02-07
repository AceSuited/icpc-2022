import sys
input = lambda:sys.stdin.readline().strip()

n,m = map(int,input().split())
seq = []
cand = []
for _ in range(n):
    seq.append(int(input()))
for _ in range(m):
    cand.append(int(input()))
seq.sort()



def solve_lower(num):
    start = 0
    end = len(seq) - 1
    ret = -1
    while start <= end:
        mid = (start + end) // 2
        if seq[mid] >= num:
            ret = mid
            end = mid - 1
        else:
            start = mid + 1
    if num == seq[ret]:
        return ret
    else:
        return -1


for num in cand:

    print((solve_lower(num)))