import sys
input = lambda: sys.stdin.readline()

n = int(input())

container =[1, 2]

for i in range(1, n):
    container.append(container[i] + container[i-1])

print(container[n-1] % 10007)
