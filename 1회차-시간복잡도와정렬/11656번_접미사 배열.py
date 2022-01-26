import sys
input = lambda:sys.stdin.readline().strip()

word = input()
suffix = []

for i in range(len(word)):
    suffix.append(word[i:])
suffix.sort()

for suff in suffix:
    print(suff)
