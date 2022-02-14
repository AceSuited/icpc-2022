import heapq
import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

max_heap = []
min_heap = []
cnt = 0
max_heap.append((-nums[0],nums[0]))
print(nums[0])
for i in range(1,n):

    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, nums[i])
        if max_heap[0][1] > min_heap[0]:
            pop = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-pop, pop))
            pop = heapq.heappop(max_heap)[1]
            heapq.heappush(min_heap,pop)

    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, (-nums[i], nums[i]))
        if max_heap[0][1] > min_heap[0]:
            pop = heapq.heappop(max_heap)[1]
            heapq.heappush(min_heap,pop)
            pop = heapq.heappop(min_heap)
            heapq.heappush(max_heap,(-pop,pop))
    else:
        heapq.heappush(min_heap, nums[i])
        if max_heap[0][1] > min_heap[0]:
            pop = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-pop, pop))

    if len(max_heap) >= len(min_heap):
        print(max_heap[0][1])
    else:
        print(min_heap[0])