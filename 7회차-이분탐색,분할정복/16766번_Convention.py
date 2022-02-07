import sys
input = lambda:sys.stdin.readline().strip()


n,m,c = map(int,input().split())

cows = list(map(int, input().split()))

cows.sort()

def possible(wait_limit):

    first_cow = cows[0]
    seat_left = c - 1
    bus_left = 1
    for i in range(1, n):
        if cows[i] - first_cow <= wait_limit and seat_left > 0:
            seat_left -= 1
        else:
            first_cow = cows[i]
            seat_left = c - 1
            bus_left += 1

    if bus_left > m:
        return False
    return True




def solve():
    start = 0
    end = max(cows)
    ret = -1
    while start <= end:
        half = (start + end) // 2
        if possible(half):
            end = half - 1
            ret = half
        else:
            start = half + 1
    return ret

print(solve())

