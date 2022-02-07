from collections import deque
n = int(input())

dq = deque()
for i in range(n, 0, -1):
    dq.append(i)

ans = [0 for _ in range(1000001)]


t = list(map(int, input().split()))
for i in range(n):
    now = t[i]

    if now == 1:
        ans[dq.pop()] = n - i
    elif now == 2:
        a = dq.pop()
        ans[dq.pop()] = n - i
        dq.append(a)
    elif now == 3:
        ans[dq.popleft()] = n - i

for i in range(1, n + 1):
    print(ans[i], end=" ")