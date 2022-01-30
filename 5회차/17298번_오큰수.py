import sys
input = lambda:sys.stdin.readline().strip()


n = int(input())
seq = list(map(int,input().split()))
ans = [-1 for _ in range(n)]
stack = []
for i in range(n):
    current = seq[i]
    if stack and stack[-1][1] < current:
        while stack and stack[-1][1] < current:
            ans[stack.pop()[0]] = current

    stack.append([i,current])

print(*ans)