import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())

datas = []
for _ in range(n):
    data = input().split()
    datas.append(data)



for j in range(n):
    data = datas[j]
    lw = "." + data[0]
    rw = "." + data[1]
    word = "." + data[2]

    container = [[0 for _ in range(len(rw))] for _ in range(len(lw))]
    container[0][0] = True

    for i in range(len(rw)):
        if rw[i] == word[i]:
            container[0][i] = True
        else:
            container[0][i] = False
    for i in range(len(lw)):
        if lw[i] == word[i]:
            container[i][0] = True
        else:
            container[i][0] = False

    for y in range(1, len(lw)):
        for x in range(1, len(rw)):

            if word[y + x] == rw[x] and word[y + x] == lw[y]:
                container[y][x] = container[y-1][x] or container[y][x-1]
            elif word[y + x] == rw[x]:
                container[y][x] = container[y][x - 1]
            elif word[y + x] == lw[y]:
                container[y][x] = container[y - 1][x]
            else:
                container[y][x] = False

    res = container[len(lw) - 1][len(rw) - 1]
    if res:
        print("Data set %d: yes" % (j + 1))
    else:
        print("Data set %d: no" % (j + 1))
