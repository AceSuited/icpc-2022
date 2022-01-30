import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n = int(input())

parrots = [list(input().split()) for _ in range(n)]
for _ in range(n):
    parrots[_].reverse()

ans = list(input().split())

for current in ans:
    found = False
    for i in range(n):
        if parrots[i] and parrots[i][-1] == current:
            parrots[i].pop()
            found = True
            break

    if not found:
        print("Impossible")
        sys.exit()

for i in range(n):
    if len(parrots[i]) > 0:
        print("Impossible")
        sys.exit()

print("Possible")
