import sys
input = lambda :sys.stdin.readline().strip()
n,m= map(int,input().split())
words = set()
for i in range(n):
    words.add(input())

cnt = 0
for i in range(m):
    word = input()
    if word in words:
        cnt += 1

print(cnt)