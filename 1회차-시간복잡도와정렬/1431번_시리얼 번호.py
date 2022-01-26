import sys

def sum_serial(serial):
    sum = 0
    for char in serial:
        if char.isdigit():
            sum += int(char)
    return sum


input = lambda:sys.stdin.readline().strip()

first = []
second = []
third = []

n = int(input())

serials = []

for _ in range(n):
    serials.append(input())

serials.sort(key = lambda x : (len(x), sum_serial(x), x))

# for i in range(len(serials)):
#     for j in range(i+1, n):
#         if len(serials[i]) > len(serials[j]):
#             temp = serials[i]
#             serials[i] = serials[j]
#             serials[j] = temp
#         elif len(serials[i]) == len(serials[j]):
#             sum_a = 0
#             sum_b = 0
#
#             for char in serials[i]:
#                 if char.isdigit():
#                     sum_a += int(char)
#             for char in serials[j]:
#                 if char.isdigit():
#                     sum_b += int(char)
#             if sum_a > sum_b:
#                 temp = serials[i]
#                 serials[i] = serials[j]
#                 serials[j] = temp
#             elif sum_a == sum_b:
#                 for a,b in zip(serials[i], serials[j]):
#                     if a > b:
#                         temp = serials[i]
#                         serials[i] = serials[j]
#                         serials[j] = temp
#                         break
#                     elif a < b:
#                         break


for serial in serials:
    print(serial)


