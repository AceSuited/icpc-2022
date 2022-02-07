import sys
input = lambda:sys.stdin.readline().strip()

k = int(input())

length = [1]

if k == 1:
    print(0)
    sys.exit()
while k > length[-1]:
    length.append(length[-1] * 2)

cnt = 0

def solve(leng,k):
    global cnt
    half = leng // 2

    if leng == 1:
        if k == 1:
            ans = False
        else:
            ans = True
        if cnt % 2 ==0:
            print(int(ans))
        else:
            print(int(not ans))
        return
    if k > half:
        cnt += 1
        solve(half, k - half)

    else:
        solve(half, k)

solve(length[-1], k)