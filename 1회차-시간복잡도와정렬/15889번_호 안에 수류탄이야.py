import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
soldier = list(map(int, input().split()))
distance = list(map(int, input().split()))

pairs = []
for i in range(n - 1):
    pairs.append((soldier[i], distance[i]))

soldier.reverse()
pairs.reverse()

visitable = [False for _ in range(n - 1)]

for i in range(n - 1):
    for j in range(i, n - 1):
        if pairs[j][0] + pairs[j][1] >= soldier[i]:
            visitable[i] = True
            break

for _ in visitable:
    if not _:
        print("엄마 나 전역 늦어질 것 같아")
        sys.exit()
print("권병장님, 중대장님이 찾으십니다")
