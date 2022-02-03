import sys
input = lambda:sys.stdin.readline().strip()

n, s = map(int,input().split())
seq = list(map(int,input().split()))


cnt = 0

visited = [False for _ in range(n)]

def solve(start,picked,depth, leng):

    global cnt


    if depth == leng:

        if sum(picked) == s:

            cnt += 1
        return

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            picked.append(seq[i])
            solve(i,picked, depth + 1, leng)
            picked.pop()
            visited[i] = False

for i in range(1, n + 1):
    solve(0,[], 0, i)

print(cnt)