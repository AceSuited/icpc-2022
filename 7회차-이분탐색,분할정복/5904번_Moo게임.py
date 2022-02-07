import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

length = [3]

idx = 1
while n > length[-1]:
    length.append(length[-1] * 2 + idx + 3)
    idx += 1

def divide(n, k):
    if n == 1:
        return "m"
    elif n == 2 or n == 3:
        return "o"

    if length[k - 1] + 1 == n:
        return "m"
    elif length[k - 1] + 1 < n <= length[k - 1] + k + 3:
        return "o"
    elif n < length[k - 1] + 1:
        return divide(n, k - 1)
    elif n > length[k - 1] + k + 3:
        return divide(n - length[k - 1] - k - 3, k - 1)

print(divide(n, idx - 1))
