import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())

cards = list(map(int,input().split()))
cards.sort()
m = int(input())
targets = list(map(int,input().split()))
def lower_bound(target):
    left = 0
    right = len(cards) - 1
    ret = len(cards)
    while left <= right:
        half = (left + right) // 2
        if cards[half] >= target:
            right = half - 1
            ret = half
        else:
            left = half + 1
    return ret

def upper_bound(target):
    left = 0
    right = len(cards) - 1
    ret = len(cards)
    while left <= right:
        half = (left + right) // 2
        if cards[half] > target:
            right = half - 1
            ret = half
        else:
            left = half + 1
    return ret

ans = []
for target in targets:
    cnt = upper_bound(target) - lower_bound(target)

    ans.append(cnt)

print(*ans)


