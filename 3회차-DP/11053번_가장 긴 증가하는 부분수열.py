import sys
input= lambda:sys.stdin.readline().strip()

n = int(input())
seq = list(map(int,input().split()))
mem = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j]:
            mem[i] = max(mem[i],  mem[j] + 1)

print(max(mem))