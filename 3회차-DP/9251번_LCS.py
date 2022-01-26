import sys
input = lambda: sys.stdin.readline().strip()

word_a = input()
word_b = input()

len_a = len(word_a)
len_b = len(word_b)

mem = [[0 for _ in range(len_a + 1)] for _ in range(len_b + 1)]

for y in range(1, len_b + 1):
    for x in range(1, len_a + 1):

        if word_a[x - 1] == word_b[y - 1]:
            mem[y][x] = mem[y-1][x-1] + 1
        else:
            mem[y][x] = max(mem[y-1][x], mem[y][x-1])

print(mem[-1][-1])