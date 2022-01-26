import sys
input = lambda: sys.stdin.readline().strip()


n = int(input())
seq = list(map(int,input().split()))
seq_sort = list((sorted(set(seq))))

dict ={}

for i in range(len(seq_sort)):
    dict[seq_sort[i]] = i

for i in range(n):
    print(dict[seq[i]], end = " ")