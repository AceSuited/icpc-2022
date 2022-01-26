import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
cases = []
for _ in range(n):

    pair = input().split()
    cases.append(pair)

for case in cases:
    alpha_map = [[0] * 26 for _ in range(2)]
    anagram = True
    for i in range(2):
        for char in case[i]:
            alpha_map[i][ord(char) - ord('a')] += 1
    for i in range(26):
        if alpha_map[0][i] != alpha_map[1][i]:
            anagram = False
            break
    if not anagram:
        print(case[0], "&", case[1], "are NOT anagrams.")
    else:
        print(case[0], "&", case[1], "are anagrams.")