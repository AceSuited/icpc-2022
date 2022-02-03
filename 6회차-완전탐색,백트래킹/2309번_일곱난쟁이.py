import sys
input = lambda:sys.stdin.readline().strip()
from itertools import combinations


dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

comb = combinations(dwarfs,7)
for term in comb:
    if sum(term) == 100:
        ans = sorted(list(term))
        for dwar in ans:
            print(dwar)
        break