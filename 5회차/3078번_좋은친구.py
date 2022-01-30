import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque
n, k = map(int,input().split())

friends = []
dic = dict()
for i in range(n):
    line = input()
    friends.append(line)
    dic[len(line)] = 0

deq = deque([])

cnt = 0
for i in range(n):
    friend = friends[i]

    if deq and i - deq[0][0] > k:
        bye = deq.popleft()
        dic[len(bye[1])] -= 1

    cnt += dic[len(friend)]
    dic[len(friend)] += 1
    deq.append([i,friend])

print(cnt)

