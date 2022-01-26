import sys
input = lambda: sys.stdin.readline().strip()

n, m= map(int,input().split())

seq = list(map(int,input().split()))
cnt = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += seq[j]
        if sum == m:
            cnt +=1
            break
        elif sum > m:
            break

print(cnt)