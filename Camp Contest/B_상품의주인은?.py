import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
a = []
b = []
c = []
d = []
visited = [False for _ in range(n + 1)]
for _ in range(n):
    student, a_, b_, c_, d_ = map(int, input().split())
    a.append((a_, student))
    b.append((b_, student))
    c.append((c_, student))
    d.append((d_, student))

res = []
a.sort(key=lambda x: (-x[0], x[1]))
res.append(a[0][1])
visited[a[0][1]] = True

b.sort(key=lambda x: (-x[0], x[1]))
for i in range(n):
    if not visited[b[i][1]]:
        res.append(b[i][1])
        visited[b[i][1]] = True
        break

c.sort(key=lambda x: (-x[0], x[1]))
for i in range(n):
    if not visited[c[i][1]]:
        res.append(c[i][1])
        visited[c[i][1]] = True
        break
d.sort(key=lambda x: (-x[0], x[1]))
for i in range(n):
    if not visited[d[i][1]]:
        res.append(d[i][1])
        visited[d[i][1]] = True
        break

print(*res)