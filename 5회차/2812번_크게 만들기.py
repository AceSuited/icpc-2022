import sys
input = lambda: sys.stdin.readline().strip()

n, k = map(int,input().split())
number = list(map(int,list(input())))

stack = [number[0]]

for i in range(1,n):
  current = number[i]
  if stack[-1] < current:
      while stack and stack[-1] < current and k > 0:
          stack.pop()
          k -= 1
  stack.append(current)

while k > 0:
    stack.pop()
    k -= 1
for num in stack:
    print(num,end="")

# 211189
