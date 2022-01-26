import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
seq = list(map(int, input().split()))

mem = [_ for _ in seq]
for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            mem[i] = max(mem[i], mem[j] + seq[i])

print(max(mem))
