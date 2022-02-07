import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque
n = int(input())
seq_origin = []
for _ in range(n):
    seq_origin.append(int(input()))

seq_sorted = sorted(seq_origin)
seq_origin = deque(seq_origin)

picked = [deque([seq_origin[0]])]
for i in range(1, n):
    current = seq_origin[i]
    idx = seq_sorted.index(current)
    found = False
    for deq in picked:
        if idx == seq_sorted.index(deq[0]) - 1:
            found = True
            deq.appendleft(current)
        elif idx == seq_sorted.index(deq[-1]) + 1:
            found = True
            deq.append(current)


    if not found:
        picked.append(deque([current]))




print(len(picked))

