import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
res = []
iters = []
iters.append("for")
iters.append("while")
for _ in range(n):
    code = input()
    temp = 0
    for iter in iters:
        temp += code.count(iter)

    res.append(temp)

print(max(res))