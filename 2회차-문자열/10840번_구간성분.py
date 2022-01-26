import sys

input = lambda: sys.stdin.readline().strip()

sa = input()
sb = input()

p = 1501
m = 1344674407370965516


p_values = [1]

pow_p = 1
for i in range(25):
    pow_p = (pow_p * p) % m
    p_values.append(pow_p)

def hash(word, start, end):
    hash_value = 0
    for i in range(start, end):
        hash_value += p_values[ord(word[i]) - ord('a')]
    return hash_value


if len(sa) >= len(sb):
    length = len(sb)
else:
    length = len(sa)

for i in range(length, 0, -1):
    container = set()
    hash_val = 0

    first = p_values[ord(sa[0]) - ord('a')]
    hash_val = hash(sa, 0, i)
    container.add(hash_val)
    for j in range(1, len(sa) - i + 1):

        hash_val -= first
        hash_val += p_values[ord(sa[j + i - 1]) - ord('a')]
        first = p_values[ord(sa[j]) - ord('a')]
        container.add(hash_val)

    first = p_values[ord(sb[0]) - ord('a')]
    hash_val = hash(sb, 0, i)
    if hash_val in container:
        print(i)
        exit()

    for j in range(1, len(sb) - i + 1):
        hash_val -= first
        hash_val += p_values[ord(sb[j + i - 1]) - ord('a')]
        first = p_values[ord(sb[j]) - ord('a')]
        if hash_val in container:
            print(i)
            exit()
print(0)