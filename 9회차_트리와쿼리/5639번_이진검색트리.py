import sys
input = lambda:sys.stdin.readline().strip()
sys.setrecursionlimit(10**5)



datas =[]
while True:
    try:
        datas.append(int(input()))
    except:
        break

visited = [False for _ in range(len(datas))]
def trav(start, end):

    if start >= end:
        return
    visited[start] = True
    current = datas[start]
    idx = start + 1

    for i in range(start + 1, end):
        if not visited[i] and datas[i] > current:
            visited[i] = True
            idx = i
            break

    trav(start + 1, idx)
    trav(idx, end)
    print(current)

visited[0] = True
trav(0, len(datas))