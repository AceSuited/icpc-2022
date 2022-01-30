import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
coords = []
for _ in range(n):
    coords.append(list(map(int,input().split())))


coords.append([0, 0])
H = max(coords, key=lambda x: x[1])[1]


cnt = 0
stack = []

for i in range(0, n + 1):

    while stack and stack[-1] > coords[i][1]:
        stack.pop()
        cnt += 1
    if stack and stack[-1] == coords[i][1]:
        continue

    stack.append(coords[i][1])
    
print(cnt)



