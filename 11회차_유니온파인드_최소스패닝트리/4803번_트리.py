import sys
input = lambda:sys.stdin.readline().strip()
sys.setrecursionlimit(10**5)
datas = []
n, m = map(int,input().split())
while not (n == 0 and m == 0):
    try:
        case = []
        case.append([n,m])
        for i in range(m):
            case.append(list(map(int,input().split())))
        datas.append(case)
        n, m = map(int, input().split())
    except:
        break


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
        roots[y] = x
for test in range(len(datas)):
    case = datas[test]

    n, m = case[0]

    roots = [i for i in range(n+1)]
    cycles =set()
    cnt = n

    notTree = False
    for i in range(1, m + 1):

        s, e = case[i]
        if find(s) == find(e):
            cycles.add(s)
            cycles.add(e)
        union(s, e)


    trees = set(find(i) for i in roots)
    cnt = len(trees) - 1
    visited = [False for  _ in range(n + 1)]

    for node in cycles:
        x = find(node)
        if not visited[x] and x in trees:
            visited[x] = True
            cnt -= 1

    if cnt == 0:
        print("Case %d: No trees." % (test + 1))
    elif cnt == 1:
        print("Case %d: There is one tree." % (test + 1))
    else:
        print("Case %d: A forest of %d trees." % (test + 1, cnt))


