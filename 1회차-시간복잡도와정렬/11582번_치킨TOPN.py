import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)

n = int(input())
stores = list(map(int,input().split()))
k = int(input())

temp = [0 for _ in range(n)]
def merge_sort(left, right):
    if left == right:
        return

    mid = (left + right) // 2
    merge_sort(left, mid)
    merge_sort(mid + 1, right)
    merge(left, right)

def merge(left, right):
    if (right - left) >(n/k):
        return
    mid = (left + right) // 2
    idx_left = left
    idx_right = mid + 1
    idx_temp = 0

    while idx_left <= mid and idx_right <= right:
        if stores[idx_left] <= stores[idx_right]:
            temp[idx_temp] = stores[idx_left]
            idx_left += 1
            idx_temp += 1
        else:
            temp[idx_temp] = stores[idx_right]
            idx_right += 1
            idx_temp += 1
    while idx_left <= mid:
        temp[idx_temp] = stores[idx_left]
        idx_temp += 1
        idx_left += 1
    while idx_right <= right:
        temp[idx_temp] = stores[idx_right]
        idx_right += 1
        idx_temp += 1
    for i in range(left, right + 1):
        stores[i] = temp[i - left]


merge_sort(0, n - 1)
print(*stores)
