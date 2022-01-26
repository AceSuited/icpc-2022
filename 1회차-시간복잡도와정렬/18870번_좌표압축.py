import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
init = list(map(int,input().split()))
sorted_init = sorted(set(init))
dic = dict()

for i in range(len(sorted_init)):
    dic[sorted_init[i]] = i

temp = []
for num in init:
    temp.append(dic[num])

for num in temp:
    print(num, end=" ")