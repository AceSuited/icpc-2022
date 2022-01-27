import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int,input().split())
cakes = list(map(int,input().split()))


cakes.sort(key=lambda x: x // 10)
cakes.sort(key=lambda x: x % 10)
cnt = 0

for i in range(n):
    cake = cakes[i]


    if cake>10:
        while cake > 10 and m > 0:
            cake -= 10
            m -= 1
            cnt += 1
            if cake == 10:
                cnt += 1
                cake -= 10
    elif cake == 10:
        cnt += 1
print(cnt)

