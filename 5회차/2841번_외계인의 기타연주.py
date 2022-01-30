import sys
input = lambda:sys.stdin.readline().strip()
n, p = map(int,input().split())

score = []
guitar = []

for _ in range(n):
    score.append(list(map(int,input().split())))

for _ in range(6):
    guitar.append([])
cnt = 0

for melody in score:
    line, prat = melody
    line -= 1
    while guitar[line] and guitar[line][-1] > prat:
        cnt += 1
        guitar[line].pop()
    if guitar[line] and guitar[line][-1] == prat:
        continue
    cnt += 1
    guitar[line].append(prat)

print(cnt)