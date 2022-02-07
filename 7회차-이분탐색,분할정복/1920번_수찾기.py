import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
seq = list(map(int,input().split()))
m = int(input())
cand = list(map(int,input().split()))

seq.sort()
def solve(num):
    start = 0
    end = len(seq) - 1
    while start <= end:
        mid = (start + end) // 2
        if seq[mid] < num:
            start = mid + 1
        elif seq[mid] > num:
            end = mid - 1
        else:
            return 1
    return 0


for num in cand:
    print(solve(num))