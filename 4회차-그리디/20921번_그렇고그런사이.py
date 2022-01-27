import sys
input = lambda: sys.stdin.readline().strip()

n, k = map(int,input().split())

seq = [x + 1 for x in range(n)]
if k == 0:
    print(*seq)
    sys.exit()
cnt = 0
for i in range(n - 1):
    for j in range(i,n - 1):
        seq[i], seq[j + 1] = seq[j + 1], seq[i]

        cnt += 1
        if cnt == k:
            print(*seq)
            sys.exit()

print(*seq)

# 1 2 3 4 5  0
# 2 1 3 4 5  1
# 3 1 2 4 5  2
# 4 1 2 3 5  3
# 5 1 2 3 4  4
# 5 2 1 3 4  5
# 5 3 1 2 4  6
# 5 4 1 2 3  7
# 5 4 2 1 3  8
# 5 4 3 1 2  9
