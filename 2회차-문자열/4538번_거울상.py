import sys

input = lambda: sys.stdin.readline().strip()

words = []

stop = False
while True:
    word = input()
    if word == "#":
        break
    words.append(word)

mirrors = {'b': 'd', 'd': 'b', 'p': 'q', "q": "p", "w": "w", "x": "x", "o": "o", "i": "i", "v": "v"}

for word in words:
    res = []
    inval = False
    for i in range(len(word)):
        try:
            res.append(mirrors[word[i]])
        except KeyError as e:
            inval = True
            print("INVALID")
            break

    if inval:
        continue
    res.reverse()

    for ch in res:
        print(ch, end="")
    print()
