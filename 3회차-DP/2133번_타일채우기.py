import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())

mem = [0 for _ in range(32)]
mem[0] = 1

for i in range(2, 32, 2):
    mem[i] = mem[i-2] * 3 + sum(mem[:i-2]) * 2

print(mem[n])