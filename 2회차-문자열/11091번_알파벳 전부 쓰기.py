import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
#

def inRange(char):
    if ord('a')<=ord(char)<= ord('z'):
        return True
    return False
sentences = []

for _ in range(n):
    sentences.append(input().lower())

for sentence in sentences:

    visited = [False] * 26

    for char in sentence:
        if inRange(char):
            visited[ord(char) - ord('a')] = True

    res = []
    for i in range(len(visited)):
        if not visited[i]:
            res.append(chr(i + ord('a')))
    res.sort()
    if len(res) == 0:
        print("pangram")
    else:
        print("missing", end = " ")
        for char in res:
            print(char, end="")
        print()