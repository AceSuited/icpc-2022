import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque

brackets = list(input())

a = brackets.count("(")
b = brackets.count(")")


stack = deque([])

prob = []
for i in range(len(brackets)):
    current = brackets[i]
    if current == "(":
        stack.append((current,i))
    else:
        if stack:
            term = stack.pop()
        else:
            prob = [current, i]
    if not stack:
        clear = i
if len(stack) > 0:
    prob = stack.pop()

ans = 0
if prob[0] == "(":
    for i in range(prob[1], len(brackets)):
        if brackets[i] == "(":
            ans += 1
elif prob[0] == ")":
    for i in range(len(brackets)-1, clear, -1):
        if brackets[i] == ")":
            ans += 1

print(ans)
