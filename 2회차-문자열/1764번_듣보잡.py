import sys
input = lambda :sys.stdin.readline().strip()

n, m = map(int,input().split())

hear = set()
see = set()

p = 53
mod = 1e9 + 9
for _ in range(n):
    hear.add(input())

for _ in range(m):
    see.add(input())


answer = list(hear & see)
answer.sort()


print(len(answer))
for wo in answer:
    print(wo)