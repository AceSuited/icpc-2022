import copy
import heapq
import sys
from collections import defaultdict
input = lambda:sys.stdin.readline()

n = int(input())

probs= [tuple(map(int,input().split())) for _ in range(n)]
m = int(input())
instructions = [input().split() for _ in range(m)]

prob_level = defaultdict(int)
problems_hard = []
problems_easy = []

exist = [False for _ in range(100002)]

for p in probs:
    heapq.heappush(problems_easy, (p[1],p[0]))
    heapq.heappush(problems_hard, (-p[1],-p[0]))
    exist[p[0]] = True
    prob_level[p[0]] = p[1]


for inst in instructions:
    if inst[0] == "add":
        heapq.heappush(problems_easy, (int(inst[2]), int(inst[1])))
        heapq.heappush(problems_hard, (-int(inst[2]), -int(inst[1])))
        prob_level[int(inst[1])] = int(inst[2])
        exist[int(inst[1])] = True

    if inst[0] == "recommend":
        if int(inst[1]) == 1:
            while (problems_hard and not exist[-problems_hard[0][1]]) or -problems_hard[0][0] != prob_level[-problems_hard[0][1]]:
                heapq.heappop(problems_hard)

            print(-problems_hard[0][1])

        elif int(inst[1]) == -1:
            while (problems_easy and not exist[problems_easy[0][1]]) or problems_easy[0][0] != prob_level[problems_easy[0][1]]:
                heapq.heappop(problems_easy)
            print(problems_easy[0][1])
    if inst[0] == "solved":
        exist[int(inst[1])] = False
        prob_level[int(inst[1])] = 0

