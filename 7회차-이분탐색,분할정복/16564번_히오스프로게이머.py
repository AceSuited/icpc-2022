import sys
input =lambda:sys.stdin.readline().strip()
n, k = map(int,input().split())

characters = [int(input()) for _ in range(n)]

start = min(characters)

def determine(target):
    remain = k
    for character in characters:
        if character <= target:
            remain -= target - character
        if remain < 0:
            return False

    return True


def parameter_search(start, end):

    ret = 0
    while start <= end:
        half = (start + end) // 2
        if determine(half):
            ret = half
            start = half + 1
        else:
            end = half - 1

    return ret

print(parameter_search(start, 2000000000))
