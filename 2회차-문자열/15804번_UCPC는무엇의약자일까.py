import sys
input = lambda:sys.stdin.readline().strip()

sentence = input()

visited = [False] * 4

words =["C", "P", "C", "U"]

current = words[-1]
for char in sentence:
    if char == current:
        words.pop()
        if words:
            current = words[-1]
        else:
            print("I love UCPC")
            sys.exit()


print("I hate UCPC")