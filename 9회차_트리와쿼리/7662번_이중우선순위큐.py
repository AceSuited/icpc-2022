import heapq
import sys
input = lambda:sys.stdin.readline().strip()

t = int(input())
cases = []

for _ in range(t):

    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False for _ in range(k)]
    for i in range(k):
        case = input().split()
        op_code = case[0]
        arg = int(case[1])

        if op_code == "I":
            heapq.heappush(min_heap, (arg, i))
            heapq.heappush(max_heap, (-arg, i))
            visited[i] = True
        else:
            if arg == 1:

                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited[heapq.heappop(max_heap)[1]] = False
            elif arg == -1:

                    while min_heap and not visited[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                    if min_heap:
                        visited[heapq.heappop(min_heap)[1]] = False

    while min_heap and visited[min_heap[0][1]] == False:
        heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]] == False:
        heapq.heappop(max_heap)

    if len(max_heap) == 0 or len(min_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])