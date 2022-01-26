import sys
input = lambda:sys.stdin.readline().strip()

word = input()
suffixes = []

for i in range(len(word)):
    suffixes.append(word[i:])

suffixes.sort()

for suffix in suffixes:
    print(suffix)