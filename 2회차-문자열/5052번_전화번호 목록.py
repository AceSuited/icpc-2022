# import sys
# input = lambda:sys.stdin.readline().strip()
#
# t = int(input())
# cases = []
# for _ in range(t):
#     case = []
#     n = int(input())
#     for _ in range(n):
#         case.append((input()))
#
#     case.sort()
#     cases.append(case)
#
# p = 59
# m = 1e18+9
#
# def hash(word):
#     global mem
#     hash_value = 0
#     for i in range(len(word)):
#         hash_value = (hash_value * p + ord(word[i])) % m
#         if hash_value in mem:
#             return False
#
#     mem.add(hash_value)
#     return True
#
#
# for case in cases:
#     mem = set()
#     first = hash(case[0])
#     res = True
#
#     for i in range(1, len(case)):
#
#         if not hash(case[i]):
#             res = False
#             break
#     if res:
#         print("YES")
#     else:
#         print("NO")
#
#


import sys
input = lambda:sys.stdin.readline().strip()

t = int(input())
cases = []
for _ in range(t):
    case = []
    n = int(input())
    for _ in range(n):
        case.append((input()))

    case.sort()
    cases.append(case)
for case in cases:
    flag = True
    for i in range(len(case) - 1):
        if case[i] == case[i + 1][:len(case[i])]:

            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
#
