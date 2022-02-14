import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
k, p = map(int, input().split())

array = [-1 for i in range(n + 1)]

upnum = k
downnum = k - 1
num = 0


def insert_children(idx):
    global downnum
    downnum += 1
    if downnum > n:
        print(-1)
        sys.exit(0)
    array[idx] = downnum
    if idx * 2 <= n:
        insert_children(idx * 2)
    if idx * 2 + 1 <= n:
        insert_children(idx * 2 + 1)


def insert_ancestors(idx):
    global upnum
    while idx // 2 > 0:
        idx = idx // 2
        upnum -= 1
        array[idx] = upnum

    if upnum <= 0:
        print(-1)
        sys.exit()


def flip(idx):
    while idx > 1:
        if array[idx] < array[idx // 2]:
            array[idx], array[idx // 2] = array[idx // 2], array[idx]
        idx = idx // 2


def insert_rest(idx):
    global num

    num += 1
    if num == upnum:
        num = downnum + 1
    array[idx] = num
    flip(idx)
    if idx * 2 <= n:
        insert_rest(idx * 2)
    elif idx * 2 + 1 <= n:
        insert_rest(idx * 2 + 1)


idx = p
insert_children(idx)

insert_ancestors(idx)

for i in range(1, n + 1):
    if array[i] != -1:
        continue
    else:
        insert_rest(i)

for i in range(1, n + 1):
    print(array[i])
