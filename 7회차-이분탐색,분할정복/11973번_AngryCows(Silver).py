import sys
input = lambda:sys.stdin.readline().strip()

n, k = map(int,input().split())

seq = []
for _ in range(n):
    seq.append(int(input()))

seq.sort()

def check(r):
    visited = [False] * n
    cnt = k
    for i in range(n):
        if not visited[i] and cnt > 0:
            visited[i] = True
            temp = seq[i] + r * 2
            cnt -= 1
            idx = i + 1
            while idx < n and seq[idx] <= temp:
                visited[idx] = True
                idx += 1
    for i in range(n):
        if not visited[i]:
            return False
    return True


def search():
    start = 0
    end = max(seq)
    ret = max(seq)
    while start <= end:
        half = (start + end) //2
        if check(half):
            end = half - 1
            ret = min(half, ret)
        else:
            start = half + 1
    return ret

print(search())


