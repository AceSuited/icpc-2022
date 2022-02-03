import sys
input = lambda:sys.stdin.readline().strip()

t= int(input())
cases = []
for _ in range(t):
    cases.append(list(map(int,input().split())))


for case in cases:
    n, m = case

    cnt = 0
    for i in range(n,m + 1):
        cnt += str(i).count("0")

    print(cnt)