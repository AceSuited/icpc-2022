import sys

input = lambda: sys.stdin.readline().strip()

r, c = map(int, input().split())
table = []
for _ in range(r):
    table.append(list(input()))
hash_table = [[0 for _ in range(c)] for _ in range(r)]

pow_p = 57
modulo = 1e9 + 9

for x in range(c):
    hash_table[r - 1][x] = ord(table[r - 1][x])


for x in range(c):
    p = pow_p
    for y in range(r - 2, 0, -1):
        hash_val = (ord(table[y][x])  * p) % modulo
        p = (p * pow_p) % modulo
        hash_table[y][x] = hash_val + hash_table[y + 1][x]



cnt = 0
for y in range(1, r):
    container = set()
    for x in range(c):
        if hash_table[y][x] not in container:
            container.add(hash_table[y][x])
        else:
            print(cnt)
            exit()

    cnt += 1

print(cnt)
