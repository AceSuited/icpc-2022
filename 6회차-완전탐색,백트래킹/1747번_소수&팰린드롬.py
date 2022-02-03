import sys
input = lambda: sys.stdin.readline().strip()


n = int(input())
def isPallindrome(num):
    num = list(str(num))
    half= len(num) // 2
    if len(num) % 2==0:
        start = half
    else:
        start = half + 1

    stack = num[:half]
    while stack:
        if stack.pop() != num[start]:
            return False
        start += 1

    return True

def isPrime(num):
    if num < 2: return False
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0: return False

    return True


for i in range(n, n + 100000000, 1):
    if isPrime(i) and isPallindrome(i):
        print(i)
        break