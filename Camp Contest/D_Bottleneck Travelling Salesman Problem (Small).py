import sys
from itertools import permutations
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

graph = [[] for _ in range((n+1))]
for _ in range(m):
    s, e, c = map(int,input().split())
    graph[s].append((e,c))


v = [i for i in range(1,n + 1)]

perm = permutations(v, n)


res = []
for order in perm:

    val = -1
    current = order[0]
    for i in range(1, n + 1):


        if i == n:
            next = order[0]
        else:
            next = order[i]

        found = False
        for ne, c in graph[current]:
            if ne == next:
                found = True
                if c > val:
                    val = c

        if not found:
            val = -1
            break

        current = next

    res.append([order, val])

res.sort(key = lambda x : x[1])


found = False
for e in res:
    if e[1] != -1:
        print(e[1])
        print(*e[0])
        found = True
        break


if not found:
    print(-1)