import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())


seqs = [list(input()) for _ in range(n)]

def solve(seq):
    stack =[]
    for char in seq:
        if char =="(":
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack)>0:
        return False
    return True
for seq in seqs:
    if solve(seq):
        print("YES")
    else:
        print("NO")