import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)

for i in range(len(nums) - 2):
    if nums[i] < nums[i+1] + nums[i+2]:
        print(nums[i] + nums[i+1] + nums[i+2])
        sys.exit()
    else:
        continue

print(-1)