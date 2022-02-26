import sys
input = lambda:sys.stdin.readline().strip()
sys.setrecursionlimit(10**5)
n, m = map(int,input().split())
roots = [i for i in range(n + 1)]
def find(x):
    if roots[x] == x:
        return x
    p = find(roots[x])
    roots[x] = p
    return roots[x]

def union(x,y):
    x = find(x)
    y= find(y)
    if x ==y:
        return
    else:
        roots[x] = y
for _ in range(m):
    op, a,b =  map(int,input().split())
    if op == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")