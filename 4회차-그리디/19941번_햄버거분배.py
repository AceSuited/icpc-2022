import sys
input = lambda:sys.stdin.readline().strip()

n, k = map(int,input().split())

table = list(input())
people = []
hamburgers = [False] * n

for i in range(n):
    if table[i] == "H":
        hamburgers[i] = True
    else:
        people.append(i)

cnt = 0

for person in people:

    start = person - k
    end = person + k + 1
    if start < 0:
        start = 0
    if end > n:
        end = n

    hamburgers[person] = "P"
    for i in range(start, end):
        if hamburgers[i] == True:
            hamburgers[i] = False
            cnt += 1
            break

print(cnt)