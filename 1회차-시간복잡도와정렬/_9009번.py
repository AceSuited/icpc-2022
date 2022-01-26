import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
fib = [1,1,2]
for num in nums:
    ans = []
    while True:
        if num >= fib[-1] + fib[-2]:
            fib.append(fib[-1] + fib[-2])
        else:
            break
    for i in range(len(fib) - 1, 0, -1):
        if num - fib[i] >= 0:
            num -= fib[i]
            ans.append(fib[i])
    ans.reverse()
    print(*ans)