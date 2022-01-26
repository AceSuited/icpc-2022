import sys
input = lambda: sys.stdin.readline().strip()

p = 53
mod = 1e9 + 9
def hash(word):
    hash_value = 0
    for i in range(len(word)):
        hash_value  = (hash_value * p + ord(word[i])) % mod

    return hash_value

n,m = map(int,input().split())

s = set()
check = []
for _ in range(n):
    s.add(hash(input()))
cnt = 0
for _ in range(m):
    check.append(hash(input()))

cnt = 0
for word in check:
    if word in s:
        cnt += 1

print(cnt)
