import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
trees = list(map(int,input().split()))

if sum(trees) % 3 != 0:
    print("NO")
    sys.exit()

origin_sum = sum(trees)
times = sum(trees) / 3
cnt = 0

for i in range(len(trees)):
    cnt += trees[i] // 2
    trees[i] = trees[i] % 2


times -= sum(trees)
origin_sum -= 3 * sum(trees)

if origin_sum >= 0 and times * 3 == origin_sum:
    print("YES")
else:
    print("NO")


