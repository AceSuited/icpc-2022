import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

words = []
for i in range(n):
    words.append(input())


def sum_digit(word):
    sum = 0
    for char in word:
        if char.isdigit():
            sum += int(char)
    return sum


words.sort(key=lambda x: (len(x), sum_digit(x), x))

for word in words:
    print(word)
