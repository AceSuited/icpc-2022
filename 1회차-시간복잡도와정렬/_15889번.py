import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
soldiers = list(map(int,input().split()))
ranges = list(map(int, input().split()))

info = []

for i in range(n-1):
    info.append((soldiers[i],ranges[i]))

soldiers.reverse()
info.reverse()

possible = [False] * n
possible[-1] = True
for i in range(n-1):
    for j in range(i,n-1):
        if soldiers[i] <= info[j][0] + info[j][1]:
            possible[i] = True
            break

for _ in possible:
    if not _:
        print("엄마 나 전역 늦어질 것 같아")
        sys.exit()

print("권병장님, 중대장님이 찾으십니다")