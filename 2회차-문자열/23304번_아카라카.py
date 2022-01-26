import sys

input = lambda: sys.stdin.readline().strip()


def isPalindrome(word):
    container = list(word[:len(word) // 2])
    if len(word) % 2 == 0:
        for i in range(len(word) // 2, len(word)):
            if word[i] != container.pop():
                return False
    else:
        for i in range(len(word) // 2 + 1, len(word)):
            if word[i] != container.pop():
                return False
    return True


word = input()

def trav(word):
    half = len(word) // 2

    if len(word) == 1:
        return True

    left = word[:half]
    right = word[half:]
    if len(word) % 2 != 0:
       right = word[half + 1:]


    if left != right:
        return False
    if trav(left) and trav(right):
        return True
    else:
        return False


if trav(word):
    print("AKARAKA")
else:
    print("IPSELENTI")