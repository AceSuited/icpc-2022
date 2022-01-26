import sys

input = lambda: sys.stdin.readline()

n = int(input())
m = int(input())
s = input()

#
# def hash(substr):
#     p = 53;
#     m = 1e9 + 9
#
#     hash_val = 0
#     pow_p = 1
#
#     for i in range(len(substr)):
#         hash_val = (hash_val + (ord(substr[i]) - ord('a') + 1) * pow_p) % m
#         pow_p = (p * pow_p) % m
#
#     return hash_val
#

# def build_susbstr(n):
#     substr = "I"
#     for i in range(n):
#         substr += "OI"
#
#     return substr
#
# substr = build_susbstr(n)
# hash_substr = hash(substr)
# cnt = 0
#
# for i in range(m - len(substr) + 1):
#     current = hash(s[i:i+len(substr)])
#     if current == hash_substr:
#         cnt += 1
#
# print(cnt)
i = 1

cnt = 0
ans = 0
while i < m:
    if s[i - 1] == "I" and s[i] == "O" and s[i + 1] == "I":
        cnt += 1
        i += 1
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        cnt = 0
    i += 1

print(ans)
