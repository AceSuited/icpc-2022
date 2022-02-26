import heapq
import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())


def find(x):
    if x == roots[x]:
        return x
    else:
        roots[x] = find(roots[x])
        return roots[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    else:
        if x < y:
            roots[y] = x
        else:
            roots[x] = y



while not (n == 0 and m == 0):
    total = 0
    roots = [i for i in range(n)]
    heap = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        heapq.heappush(heap, (z, x, y))
        total += z

    cnt = 0
    ans = 0
    while cnt < n - 1:
        if heap:
            cost, s, e = heapq.heappop(heap)
            if find(s) != find(e):
                union(s, e)
                ans += cost
                cnt += 1

    print(total - ans)
    n, m = map(int, input().split())
