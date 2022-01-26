import sys

input = lambda: sys.stdin.readline().strip()

T = int(input())
data = []

for _ in range(T):
    case = []
    n = int(input())
    case.append(n)
    words = []
    for _ in range(n):
        words.append(input())
    case.append(words)
    data.append(case)


def isPalindrome(word):
    half = len(word) // 2
    word = list(word)
    stack = word[:half]
    if len(word) % 2 == 0:
        for char in word[half:]:
            if stack.pop() != char:
                return False
    else:
        for char in word[half + 1:]:
            if stack.pop() != char:
                return False

    return True

def test(case):
    n = case[0]
    words = case[1]
    for i in range(n):
        for j in range(i + 1, n):
            current = []
            current.append(words[i] + words[j])
            current.append(words[j] + words[i])
            for word in current:
                if isPalindrome(word):
                    return word
    return 0

for case in data:
   print(test(case))

