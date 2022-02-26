import sys
input = lambda: sys.stdin.readline().strip()

t, k = map(int,input().split())
questions = []
for _ in range(t):
    questions.append(int(input()))

