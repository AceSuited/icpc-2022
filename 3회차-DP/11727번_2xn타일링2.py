import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())

mem = [1,3]

for i in range(2, 1000):
    mem.append(mem[i - 1] + 2 * mem[i - 2])

print(mem[n - 1] % 10007)