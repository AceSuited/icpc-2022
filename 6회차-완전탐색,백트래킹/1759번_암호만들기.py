import sys
from itertools import combinations
input = lambda:sys.stdin.readline().strip()


n, m = map(int,input().split())
candidate = sorted(input().split())
vowel = set(['a','e','i','o','u'])

comb = list(combinations(candidate, n))
for term in comb:
    cnt_vowel = 0
    cnt_cons = 0
    for ch in term:
        if ch in vowel:
            cnt_vowel += 1
        else:
            cnt_cons += 1
    if cnt_vowel > 0 and cnt_cons > 1:
        print("".join(term))

