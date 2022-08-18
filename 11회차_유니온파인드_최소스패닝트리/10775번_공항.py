import sys
input = lambda:sys.stdin.readline().strip()

g = int(input())
p = int(input())

gis = []

roots = [i for i in range(g + 1)]
def find(x):
    if x == roots[x]:
        return x
    else:
        roots[x] = find(roots[x])
        return roots[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    else:
        if x < y:
            roots[y] = x
        else:
            roots[x] = y

for i in range(p):
    gis.append(int(input()))

cnt = 0

gates = [-1 for i in range(g + 1)]
temp = 0
for gi in gis:
    temp += 1
    gate_num = find(gi)
    if gates[gate_num] == -1:
        gates[gate_num] = temp
        cnt += 1
        if gate_num - 1 > 0:
            union(gate_num, gate_num - 1)
    else:
        break
print(cnt)