import sys
input = lambda:sys.stdin.readline().strip()


n = int(input())

for i in range(n//2, n):
    current = i
    digits = list(str(i))
    for digit in digits:
        current += int(digit)
    if current == n:
        print(i)
        sys.exit()


print(0)
