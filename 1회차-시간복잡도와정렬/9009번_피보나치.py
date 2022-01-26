import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())

nums=[]
for _ in range(n):
    nums.append(int(input()))

for num in nums:
    mem = [1, 1]
    ans = []

    while True:
        next = mem[len(mem)-1] + mem[len(mem) - 2]
        if next <= num:
            mem.append(next)
        else:
            break
    mem.sort(reverse= True)
    for i in range(len(mem)):
        if mem[i] <= num:
            num -= mem[i]
            ans.append(mem[i])
    ans.reverse()

    print(*ans)

