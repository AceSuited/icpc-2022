import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
lines =[]

for i in range(n):
    lines.append(int(input()))
lines.sort(reverse=True)
made = -1
for i in range(n - 2):
    if lines[i] < lines[i + 1] + lines[i + 2]:
        made = lines[i] + lines[i+1] + lines[i+2]
        break

print(made)