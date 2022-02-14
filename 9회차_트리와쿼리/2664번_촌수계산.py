import sys
input = lambda:sys.stdin.readline().strip()

tree =dict()
n = int(input())
s, e = map(int,input().split())
m = int(input())
for _ in range(m):
    a, b = map(int,input().split())
    if a in tree:
        tree[a].append(b)
    else:
        tree[a] = [b]
    if b in tree:
        tree[b].append(a)
    else:
        tree[b] = [a]

visited = [False for _ in range(n + 1)]
ans = -1
def trav(current, cnt):

    global ans
    if current == e:
        ans = cnt
        return

    for next in tree[current]:
        if not visited[next]:
            visited[next] = True
            trav(next, cnt + 1)


visited[s] = True
trav(s, 0)
print(ans)