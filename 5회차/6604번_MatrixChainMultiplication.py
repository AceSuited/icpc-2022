import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n = int(input())
matrixes = []
for _ in range(n):
    matrixes.append(list(map(int, input().split()[1:])))


def solve(equation):
    stack = deque([])
    ans = 0

    for char in equation:
        if char == "(":
            stack.append(char)
        elif char == ")":
            eq = []

            while stack[-1] != "(":
                eq.append(stack.pop())
            stack.pop()
            eq.reverse()
            if eq[0][1] != eq[1][0]:
                print("error")
                return
            else:
                ans += eq[0][0] * eq[0][1] * eq[1][1]
                stack.append([eq[0][0], eq[1][1]])
        else:
            idx = ord(char) - ord("A")
            stack.append(matrixes[idx])

    print(ans)


while True:
    equation = input()
    if equation == "":
        break
    else:
        solve(list(equation))
