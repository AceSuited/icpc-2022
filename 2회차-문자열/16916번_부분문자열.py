import sys

input = lambda: sys.stdin.readline().strip()

p = 53
m = 1e9 + 9


def hash(word):
    hash_value = 0

    for i in range(len(word)):
        hash_value = (hash_value * p + ord(word[i])) % m

    return hash_value


word = input()
check = input()

len_word = len(word)
len_check = len(check)

if len_word == len_check:
    if word == check:
        print(1)
        exit()
    else:
        print(0)
        exit()

hash_word = hash(word[:len_check])
hash_check = hash(check)
first = 1

for i in range(len(check) - 1):
    first = (first * p) % m
for i in range(len_word - len_check + 1):
    if hash_check == hash_word:
        print(1)
        exit()
    if i + len_check < len_word:
        hash_word = hash_word - (ord(word[i]) * first) % m
        hash_word = ((hash_word * p) % m + ord(word[i + len_check]) % m)

print(0)
