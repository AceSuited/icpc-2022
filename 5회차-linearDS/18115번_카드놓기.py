import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n = int(input())
skills = list(map(int,input().split()))
skills.reverse()
hand = deque([])
floor = deque([ _ for _ in range(n, 0, -1)])

for skill in skills:
    if skill == 1:
        hand.append(floor.pop())
    elif skill == 2:
        temp = hand.pop()
        hand.append(floor.pop())
        hand.append(temp)
    elif skill == 3:
        hand.appendleft(floor.pop())

hand.reverse()
print(*hand)
