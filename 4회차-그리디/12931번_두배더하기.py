import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
seq = list(map(int, input().split()))

cnt = 0
while True:
    done = True
    for num in seq:
        if num != 0:
            done = False
    if done:
        print(cnt)
        break

    operated = False
    for i in range(n):
        if seq[i] % 2 != 0 and seq[i] != 0:
            seq[i] -= 1
            cnt += 1
            operated = True
            break
    if not operated:
        for i in range(n):
            seq[i] = seq[i] / 2
        cnt += 1
