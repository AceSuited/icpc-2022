import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())


equation = list(input())
dic = dict()
for i in range(n):
    dic[chr(65 + i)] = int(input())


stack = []
temp = 0
for ch in equation:
    if ch.isalpha():
        stack.append(dic[ch])
    else:
        operand_a = stack.pop()
        operand_b = stack.pop()

        if ch == "*":
            stack.append(operand_b * operand_a)
        elif ch == "/":
            stack.append(operand_b / operand_a)
        elif ch == "+":
            stack.append(operand_b + operand_a)
        elif ch == "-":
            stack.append(operand_b - operand_a)


print("%.2f" %(stack[-1]))