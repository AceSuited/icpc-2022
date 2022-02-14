import sys
input = lambda:sys.stdin.readline()
sys.setrecursionlimit(10**5)

n,r,q = map(int,input().split())

tree= [[] for _ in range(n + 1)]
for _ in range(n -1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited= [False for _ in range(n + 1)]
queries = []
for _ in range(q):
    queries.append(int(input()))

cnt = [0 for _ in range(n + 1)]

def trav(start):
    found = False
    cnt[start] += 1
    for next in tree[start]:
        if visited[next] == False:
            visited[next] = True
            cnt[start] += trav(next)

    return cnt[start]
visited[r] = True
trav(r)
for query in queries:
    print(cnt[query])
