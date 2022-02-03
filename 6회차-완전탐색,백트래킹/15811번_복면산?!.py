import sys
input = lambda:sys.stdin.readline().strip()
from itertools import permutations
words = list(map(list,input().split()))

charset = set()

for word in words:
    for char in word:
        charset.add(char)

charset = list(charset)
num = len(charset)
if len(charset) > 10:
    print("NO")
    sys.exit()

def calculate(picked):

    dic = dict()
    for i in range(len(charset)):
        dic[charset[i]] = picked[i]
    converted = []
    for word in words:
        temp = 0
        for char in word:
            temp *= 10
            temp += dic[char]
        converted.append(temp)

    if converted[0] + converted[1] == converted[2]:
        print("YES")
        sys.exit()

    return

perm = (permutations([i for i in range(10)], num))

for term in perm:
    calculate(term)


print("NO")


#
# def solve(depth,picked):
#     if depth == num:
#         print(picked)
#         calculate(picked)
#         return
#
#     for i in range(10):
#         if not visited[i]:
#             picked.append(i)
#             visited[i] = True
#             solve(depth + 1, picked)
#             visited[i] = False
#             picked.pop()
#

# 문자열 연산보다 숫자 계산이 시간이 훨 빠르다.
# 변환 과정을 문자열로 처리했을때 시간초과, 숫자로 하니 시간초과가 안뜨더라.

#itertools를 사용할때는 유의하자. 만일 permutation의 결과물을 그대로 사용안하고 list()로 변환하면 엄청난 양의 메모리를 잡아먹게 되어 메모리 초과가 발생한다. 유의!
